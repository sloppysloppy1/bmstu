from misc import sbox, inv_sbox, rcon, start

from struct import pack

from numpy import empty

Nb = 4 # число столбцов
Nk = 4 # длина ключа
Nr = 10 # кол-во раундов шифрования

    
def subbytes(state, mode = 'encode'):

    if mode == 'encode':
    
        for i in range(Nb):
            for j in range(Nb):
            
                state[i][j] = sbox[state[i][j]]

    else:
        for i in range(Nb):
            for j in range(Nb):
            
                state[i][j] = inv_sbox[state[i][j]]

    return state


def shiftrows(state, mode = 'encode'):

    if mode == 'encode':
        
        for i in range(Nb):
            if i != 0:
            
                state[i] = state[i][1:] + state[i][:1]

    else:
        for i in range(Nb):
            if i != 0:
            
                state[i] = state[i][-1:] + state[i][:-1]
        

    return state


def ml(number):
    
    if number < 0x80:
        number = (number << 1)

    else:
        number = (number << 1) ^ 0x1b

    return number % 0x100


def ml3(number):

    return ml(number) ^ number


def ml9(number):

    return ml(ml(ml(number))) ^ number


def mlb(number):

    return ml(ml(ml(number))) ^ ml(number) ^ number


def mld(number):

    return ml(ml(ml(number))) ^ ml(ml(number)) ^ number


def mle(number):

    return ml(ml(ml(number))) ^ ml(ml(number)) ^ ml(number)


def mixcolumns(state, mode = 'encode'):

    if mode == 'encode':

        fixed = [['02','03','01','01'], ['01','02','03','01'],
                 ['01','01','02','03'], ['03','01','01','01']]

        for i in range(Nb):

            state_0 = (ml(state[0][i]) ^ ml3(state[1][i]) ^
                   state[2][i] ^ state[3][i])

            state_1 = (ml(state[1][i]) ^ ml3(state[2][i]) ^
                   state[0][i] ^ state[3][i])

            state_2 = (ml(state[2][i]) ^ ml3(state[3][i]) ^
                   state[0][i] ^ state[1][i])

            state_3 = (ml(state[3][i]) ^ ml3(state[0][i]) ^
                   state[2][i] ^ state[1][i])

    else:
        for i in range(Nb):

            state_0 = (mle(state[0][i]) ^ mlb(state[1][i]) ^
                   mld(state[2][i]) ^ ml9(state[3][i]))

            state_1 = (mle(state[1][i]) ^ mlb(state[2][i]) ^
                   mld(state[3][i]) ^ ml9(state[0][i]))

            state_2 = (mle(state[2][i]) ^ mlb(state[3][i]) ^
                   mld(state[0][i]) ^ ml9(state[1][i]))
            
            state_3 = (mle(state[3][i]) ^ mlb(state[0][i]) ^
                   mld(state[1][i]) ^ ml9(state[2][i]))

    state[0][i] = state_0
    state[1][i] = state_1
    state[2][i] = state_2
    state[3][i] = state_3

    return state


def addroundkey(state, roundkey):

    for i in range(Nb):
        for j in range(Nb):

            state[i][j] ^= roundkey[i][j]

    return state


def keyexpansion(key):
    
    keyschedule = empty([4, 4 * 11], dtype=object)

    for i in range(Nb):
        for j in range(Nb):
            
            keyschedule[i][j] = key[i][j]

    for j in range (Nb, Nb * (Nr + 1)):
        for i in range (Nb):
            
            if (j % Nb == 0):
                tmp = [keyschedule[row][j-1] for row in range(1, Nb)]
                tmp.append(keyschedule[0][j-1])
                
                keyschedule[i][j] = (sbox[tmp[i]] ^ keyschedule[i][j - Nb]
                                     ^ rcon[i][j // Nb - 1])
            else:
                keyschedule[i][j] = (keyschedule[i][j - 1]
                                     ^ keyschedule[i][j - Nb])

    return keyschedule


def encode(state_start, key_start):
    
    state = [[0] * Nb for i in range(Nb)]
    key = [[0] * Nb for i in range(Nb)]

    if (len(key_start) < 16):
        for i in range(len(key_start), 16):
            
            key_start += b'\x00'

    if (len(state_start) < 16):
        for i in range(len(state_start), 16):
            
            state_start += b'\x00'

    for i in range(Nb):
        for j in range(Nb):
            
            state[i][j] = state_start[i + Nb * j]
            key[i][j] = key_start[i + 4 * j]

    keyschedule = keyexpansion(key)

    state = addroundkey(state, keyschedule[:, 0:Nb])

    for i in range(1, Nr + 1):

        tmp = i * Nb
        curr_key = keyschedule[:, tmp:tmp + Nb]

        state = subbytes(state)

        state = shiftrows(state)
        
        if i != 10: 
            state = mixcolumns(state)

        state = addroundkey(state, curr_key)

    return state

                     
def decode(state_start, key_start):
    
    state = [[0] * Nb for i in range(Nb)]
    key = [[0] * Nb for i in range(Nb)]

    if (len(key_start) < 16):
        for i in range(len(key_start), 16):
            
            key_start += b'\x00'

    if (len(state_start) < 16):
        for i in range(len(state_start), 16):
            
            state_start += b'\x00'

    for i in range(Nb):
        for j in range(Nb):
            
            state[i][j] = state_start[i + Nb * j]
            key[i][j] = key_start[i + 4 * j]

    keyschedule = keyexpansion(key)

    tmp = Nr * Nb 
    state = addroundkey(state, keyschedule[:, tmp:tmp + Nb])

    for i in range(Nr - 1, -1, -1):

        tmp = i * Nb
        curr_key = keyschedule[:, tmp:tmp + Nb]

        state = shiftrows(state, 'decode')

        state = subbytes(state, 'decode')

        state = addroundkey(state, curr_key)
        
        if i != 0: 
            state = mixcolumns(state, 'decode')

    return state


if __name__ == "__main__":

    filename_in = input("input filename: ")

    file = open(filename_in, 'rb')

    temp_key = input("input key: ")

    key = bytes(temp_key, 'utf-8')

    filename_out = input("input output filename: ")

    file_out = open(filename_out, 'wb')

    option = input("encode or decode: ")
        
    while True:
            
        temp_char = file.read(16)
            
        if not temp_char:
            break

        if option == 'encode':
            result = encode(temp_char, key)

        else:
            result = decode(temp_char, key)

        for j in range(Nb):
            for i in range(Nb):
                
                file_out.write(pack("B", result[i][j]))
                
    file.close()
    file_out.close()
















                   
