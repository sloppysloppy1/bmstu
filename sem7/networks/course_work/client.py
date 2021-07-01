import tkinter as tk
import os
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
from pickle import loads

from protocol import get


HOST = input('input ip: ')             
PORT = 1237

dataint = []

stopped = False
playing = False
named = False

RATE = 44100
CHUNK = 1024 * 2

volume = 1

    
def ch_volume(val):
    global volume

    volume = int(val)/100.
  
  
def connect():
    global playing, conn_thread, s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    playing = True

    conn_thread = Thread(target=init, args=(s,))
    conn_thread.start()
    
    
def disc():
    global s, stopped, playing

    stopped = True
    playing = False
    
    s.close()
    

def init(s):
    global dataint, stopped, playing, volume, track, name
    
    audio = pyaudio.PyAudio()

    stream = audio.open(format=32,
                    channels=2,
                    rate=44100,
                    output=True)

    while playing:
        try:
            name_data = get(s)
            name, data = loads(name_data)
            chunk = np.frombuffer(data, np.uint8)
            chunk= chunk *volume

            data = chunk.astype(np.uint8)
            
            stream.write(data)
            dataint = np.array(struct.unpack(str(2* CHUNK) + 'B', data),
                               dtype = 'b')[::2] + 128
        except Exception:
            pass
            
    if stopped:
        stream.stop_stream()
        stream.close()
        audio.terminate()


def gui():
    global track, playlist, fig, line, dataint, playing, RATE, CHUNK, songtrack, name

    root = tk.Tk()

    root.title('client')
    root.geometry('600x400')
    name = ''

    trackframe = tk.LabelFrame(root,text="currently playing",font=("times new roman",15,"bold"),bg="Navyblue",fg="white",bd=5,relief=tk.GROOVE)
    trackframe.place(x=0,y=0,width=800,height=100)
    track = tk.StringVar()
    
    songtrack = tk.Label(trackframe,textvariable = track,width=30,font=("times new roman",24,"bold"),bg="orange",fg="blue")
    songtrack.grid(row=0,column=0,padx=10,pady=5)
    
    
    buttonframe = tk.LabelFrame(root,text="control panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)
    playbtn = tk.Button(buttonframe,text="CONNECT",command=connect,width=12,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=0,padx=20,pady=5)
    playbtn = tk.Button(buttonframe,text="DISCONNECT",command=disc,width=12,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=2,padx=20,pady=5)  
    vol_scale = tk.Scale(buttonframe,from_=100,to=0,command=ch_volume,orient=tk.HORIZONTAL,relief=tk.GROOVE, bg='gold', troughcolor='yellow')
    vol_scale.grid(row=0,column=5, padx=30)
    vol_scale.set(100)
                            
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
        track.set(name)
        root.update()


gui_thread = Thread(target=gui)
gui_thread.start()

gui_thread.join()

    
