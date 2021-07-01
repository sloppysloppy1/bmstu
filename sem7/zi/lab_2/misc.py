from random import random, choice, shuffle

max_len = 256
rotor_counter = 0


def get_alphabet():

    alphabet = []

    for i in range(max_len):
        alphabet.append(i)

    return alphabet


def create_rotor():

    global rotor_counter
    
    f = open('config.txt', 'a')

    f.write(str(rotor_counter) + ' ')
    rotor_counter += 1

    rotor = get_alphabet()
    
    shuffle(rotor)
    for elem in rotor:
        f.write(str(elem) + ' ')

    f.write('\n')
    f.close()


def create_reflector():

    reflector = []
    
    f = open('config.txt', 'a')

    f.write('r' + ' ')

    temp_reflector = get_alphabet()
    
    for i in range(max_len):
        
        elem = choice(temp_reflector)
        reflector.append(elem)
        temp_reflector.remove(elem)

    
    for i in range(max_len):
            f.write(str(reflector[i]) + ' ')

    f.write('\n')
    f.close()


def get_reflector():

    f = open('config.txt', 'r')

    for line in f:
        if 'r' == str(line[0]):
            reflector = list(map(int, line[1:].split()))
            
    f.close()

    return reflector 

    
def get_rotor(num):

    f = open('config.txt', 'r')

    for line in f:
        if str(num) == line[0]:
            rotor = list(map(int, line.split()))

    rotor = rotor[1:]
    
    f.close()

    return rotor 


def get_rotors():

    f = open('config.txt', 'r')

    for line in f:
        if 'b' == str(line[0]):
            rotors = list(map(int, line[1:].split()))
            
    f.close()

    return rotors

