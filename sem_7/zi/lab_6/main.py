from pickle import dump, load
from huffman import huffman, huffman_decode
from base64 import b32encode, b32decode
import sys


def to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder = 'big')


def back_to_bytes(s):
    return '0' + bin(int.from_bytes(s, byteorder = 'big'))[2:]


def encode_str():
    s = input()
    code = huffman(s)

    encoded = ''.join(code[ch] for ch in s)
    
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))
    print(encoded)


def clench(filename):
    
    with open (filename, 'rb') as f:
        text = f.read()

    code = huffman(text)

    for ch in sorted(code):
        print('{}: {} '.format(ch, code[ch]))

    encoded = to_bytes(''.join(code[ch] for ch in text))

    with open('squeezed','wb') as fs:
        fs.write(bytes(encoded))

    with open('cd','wb') as fc:
        dump(code, fc)


def unclench(filename):

    with open('squeezed','rb') as fu:
        text = fu.read()

    with open('cd','rb') as fc:
        code = load(fc)

    
    decoded = huffman_decode(back_to_bytes(text), code)
    
    with open(filename,'wb') as f1:
        f1.write(bytes(decoded))
