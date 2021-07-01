from collections import Counter, namedtuple
from heapq import heapify, heappop, heappush

class node(namedtuple('Node', ['left', 'right'])):
    
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

        
class leaf(namedtuple('Leaf', ['char'])):
    
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman(string):

    h = []

    for ch, freq in Counter(list(string)).items():
        h.append((freq, len(h), leaf(ch)))
                 
    heapify(h)

    count = len(h)
    while len(h) > 1:
        
        freq1, _count1, left = heappop(h)
        freq2, _count2, right = heappop(h)
        heappush(h, (freq1  + freq2, count, node(left, right)))

        count += 1
        
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')

    return code


def huffman_decode(string, code):
    
    pointer = 0
    decoded_str = []
    
    while pointer < len(string):
        for ch in code.keys():
            if string.startswith(code[ch], pointer):
                
                decoded_str.append(ch)
                pointer += len(code[ch])
                
    return decoded_str
