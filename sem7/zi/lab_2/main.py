from random import random

from struct import pack

from misc import (max_len, get_alphabet, create_rotor, create_reflector,
get_reflector, get_rotor, get_rotors)


def first_rotor(symbol, start):

    rotor = get_rotor(0)

    temp_symbol = (symbol + start) % max_len
    
    symbol = rotor[temp_symbol]
    
    return symbol


def second_rotor(symbol, start, first_start):
    
    rotor = get_rotor(1)

    temp_symbol = ((start - first_start) + symbol) % max_len

    symbol = rotor[temp_symbol]
    
    return symbol


def third_rotor(symbol, start, second_start):
    
    rotor = get_rotor(2)
    reflector = get_reflector()

    temp_symbol = ((start - second_start) + symbol) % max_len

    symbol = (rotor[temp_symbol] - start) % max_len

    symbol = reflector.index(symbol)
 
    return symbol


def third_rotor_backw(symbol, start, second_start):

    rotor = get_rotor(2)

    symbol = (symbol + start) % max_len
    temp_symbol = rotor.index(symbol)

    symbol = (temp_symbol - (start - second_start)) % max_len

    return symbol
        

def second_rotor_backw(symbol, start, first_start):

    rotor = get_rotor(1)

    temp_symbol = rotor.index(symbol)

    symbol = (temp_symbol - (start - first_start)) % max_len
    
    return symbol


def first_rotor_backw(symbol, start):
    
    rotor = get_rotor(0)

    temp_symbol = rotor.index(symbol)

    symbol = (temp_symbol - start) % max_len

    return symbol


def ENIGMA(str_, configuration):
    
    new_str = b""
    
    for symbol in str_:

        symbol = chr(symbol)

        symbol = ord(symbol)
        
        first = configuration[0]
        second = configuration[1]
        third = configuration[2]

        symbol = int(symbol)

        first = (first + 1) % max_len

        symbol = first_rotor(symbol, first)

        if first == max_len - 1:
            second = (second + 1) % max_len

        symbol = second_rotor(symbol, second, first)

        if second == max_len - 1:
            third = (third + 1) % max_len
            
        symbol = third_rotor(symbol, third, second)

        symbol = third_rotor_backw(symbol, third, second)

        symbol = second_rotor_backw(symbol, second, first)
        
        symbol = first_rotor_backw(symbol, first)

        symbol = chr(symbol)

        new_str += pack('B', ord(symbol)) 

    return new_str


if __name__ == "__main__":
    
    cond = input("str or file: ")

    configuration = get_rotors()

    if cond == 'str':
    
        str_ = input("input str: ")
        
        print("encoded: ", ENIGMA(str_, configuration))

    else:

        filename_in = input("input filename: ")

        file = open(filename_in, 'rb')

        filename_out = input("input output filename: ")

        file_out = open(filename_out, 'wb')
        
        while True:
            
            temp_char = file.read()
            
            if not temp_char:
                break

            char = ENIGMA(temp_char, configuration)

            file_out.write(char)

        file.close()
        file_out.close()

    
