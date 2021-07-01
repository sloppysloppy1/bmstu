import socket
from struct import pack, unpack


def recvall(sock, count):
    buf  = b''

    while count:
        newbuf = sock.recv(count)
        
        if not newbuf:
            return None

        buf +=  newbuf
        count -=len(newbuf)
        
    return buf
    
    
def send(sock, data):
    length = len(data)
    
    sock.sendall(pack('!I', length))
    sock.sendall(data)


def get(sock):
    lenbuf = recvall(sock, 4)
    len, = unpack('!I', lenbuf)
    
    return recvall(sock, len)
