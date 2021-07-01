import tkinter as tk
import os
import subprocess
from threading import Thread, Event
import pyaudio
import wave
import socket
from protocol import send
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.fftpack import fft
import struct
from pickle import dumps


playing = False
paused = False
resumed = False
stopped = False

HOST = '192.168.0.104'               
PORT = 1237
s_list = []

s =''

dataint = []

CHUNK = 1024 * 2
RATE = 44100

volume = 1


def ch_volume(val):
    global volume

    volume = int(val)/100.
    
    
def play():
    global playing, play_thread
    
    curr = playlist.get(tk.ACTIVE)
    track.set(curr)

    if not playing:
        playing = True
        event = Event()
        play_thread = Thread(target=init_audio, args=(curr,event))
        play_thread.start()


def pause():
    global paused, event

    paused = True
    event.clear() 

    
def resume():
    global resumed, event
    
    event.set()


def stop():
    global playing, stream, audio, play_thread

    if playing:
        playing = False
        stopped = True
        paused = False
        resumed = False

        play_thread.join()
        

def init_conn():
    global s_list,s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    
    s_list = [s]

    print('waiting')
    while True:
        conn, addr = s.accept()
        s_list.append(conn)
        print('connected', addr)


def init_audio(name, ev):
    global stream, audio, playing, paused, event, FORMAT
    global CHANNELS, RATE, dataint, s_list, volume, s, played

    event = ev
    audio = pyaudio.PyAudio()

    try:        
        if name.find('.wav') == -1:
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.run(f"""ffmpeg -i {name} -acodec pcm_u8 -ar 44100 temp.wav""",
                           capture_output=True, text=True, input="y", startupinfo=si)
            wf = wave.open('temp.wav', 'rb')
        else:
            wf = wave.open(name, 'rb')

        FORMAT = audio.get_format_from_width(wf.getsampwidth())
        CHANNELS = wf.getnchannels()
        RATE = wf.getframerate()
        print(FORMAT, RATE, CHANNELS)

        stream = audio.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True)

        data = wf.readframes(CHUNK)

        while data != '' and playing:
            for sock in s_list[1:]:
                try:
                    name_data = dumps([name, data])
                    send(sock, name_data)
                except Exception:
                    pass
            chunk = np.frombuffer(data, np.uint8)
            chunk = chunk * volume
            
            data = chunk.astype(np.uint8)

            try:
                dataint = np.array(struct.unpack(str(2*CHUNK) + 'B', data),
                               dtype = 'b')[::2] + 128
            except Exception:
                break

            if paused:
                while not ev.isSet():
                    ev.wait()
            
            stream.write(data)
            
            data = wf.readframes(CHUNK)

        stopped = True

        if stopped:
            print('stopped')
            stop()
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
    except EOFError:
        print('cant open', name)
        playing = False

    
def gui():
    global track, playlist, fig, line, dataint, playing, RATE, CHUNK

    os.chdir("C:\\Users\\schoolboychik\\Desktop\\sco\\sem7\\networks\\course\\music")
    songtracks = os.listdir()

    root = tk.Tk()

    root.title('server')
    root.geometry('800x400')

    trackframe = tk.LabelFrame(root,text="currently playing",font=("times new roman",15,"bold"),bg="Navyblue",fg="white",bd=5,relief=tk.GROOVE)
    trackframe.place(x=0,y=0,width=600,height=100)
    track = tk.StringVar()
    track.set('  ')
    songtrack = tk.Label(trackframe,textvariable=track,width=20,font=("times new roman",24,"bold"),bg="orange",fg="blue", relief = tk.GROOVE)
    songtrack.grid(row=0,column=0,padx=10,pady=5)
    
    volume_scale = tk.Scale(trackframe,from_=100,to=0, command=ch_volume, orient = tk.HORIZONTAL, relief=tk.GROOVE, troughcolor = 'yellow', bg ='gold')
    volume_scale.grid(row=0,column=1, padx=30)
    volume_scale.set(100)
    buttonframe = tk.LabelFrame(root,text="control panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)
    playbtn = tk.Button(buttonframe,text="PLAY",command=play,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=0,padx=20,pady=5)
    playbtn = tk.Button(buttonframe,text="STOP",command=stop,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=3,padx=20,pady=5)  
    playbtn = tk.Button(buttonframe,text="RESUME",command=resume,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=2,padx=20,pady=5)
    playbtn = tk.Button(buttonframe,text="PAUSE",command=pause,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=1,padx=20,pady=5)  

    songsframe = tk.LabelFrame(root,text="songs",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    songsframe.place(x=600,y=0,width=200,height=200)

    scrol_y = tk.Scrollbar(songsframe,orient=tk.VERTICAL)
    playlist = tk.Listbox(songsframe,yscrollcommand=scrol_y.set,
                              selectbackground="gold",selectmode=tk.SINGLE,
                              font=("times new roman",12,"bold"),
                              bg="silver",fg="navyblue",bd=5,relief=tk.GROOVE)

    scrol_y.pack(side=tk.RIGHT,fill=tk.Y)
    scrol_y.config(command=playlist.yview)
    playlist.pack(fill=tk.BOTH)

    for song in songtracks:
        if song != 'temp.wav':
            playlist.insert(tk.END,song)
    
    fig2 = plt.Figure(figsize=(8,2), dpi =100)
    fig2.patch.set_facecolor('pink')
    fig2.patch.set_alpha(0.6)

    ax2 = fig2.add_subplot()
    ax2.patch.set_facecolor('orange')
    ax2.patch.set_alpha(0.2)
    
    xf = np.linspace(0, RATE, CHUNK)    
    line_fft, = ax2.semilogx(xf, np.random.rand(CHUNK), '-', lw=2)
    ax2.set_xlim(20, RATE / 2)
    ax2.get_xaxis().set_ticks([])
    ax2.get_yaxis().set_ticks([])

    canvas1 = FigureCanvasTkAgg(fig2, master=root)
    canvas1.get_tk_widget().pack(side = tk.BOTTOM)
    
    
    while True:
        if len(dataint) != 0 and playing:
            yf = fft(dataint)
            line_fft.set_ydata(np.abs(yf[0:CHUNK])  / (64 * CHUNK))
            canvas1.draw()
            canvas1.flush_events()  
        root.update()

        
conn_thread = Thread(target=init_conn)
gui_thread = Thread(target=gui)

conn_thread.start()
gui_thread.start()

conn_thread.join()
gui_thread.join()




