from __future__ import print_function
from math import sqrt, log
from base64 import b32encode, b32decode
from random import randrange, randint
from pickle import load, dump


seed_start = 2 ** 20
seed_end = 2 ** 21


def is_prime(num):

    d = 3
     
    if num % 2 == 0:
        return num == 2
    
    while d * d <= num and num % d != 0:
        d += 2
        
    return d * d > num

              
def generate_number(check_eq = 0):

    num = 10

    prime_check = is_prime(num)
    
    while prime_check != True:

        num = randint(seed_start, seed_end)

        prime_check = is_prime(num)

        if num == check_eq:
            prime_check = True

    return num


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

   
def get_keys():

    p = generate_number()
    q = generate_number(p)

    n = p * q

    f = (p-1) * (q-1)
    
    for i in range(0, seed_end + 1):
        
        if gcd(i, f) == 1 and i < f:
            e = i
            break

    for i in range(0, f):
        
        if (i * f + 1) % e == 0:
            d = (i * f + 1) // e 
            break

    return [e, d, n]


def rsa_encode(msg, keys):

    msg = msg ** keys[0] % keys[2]

    return msg


def rsa_decode(msg, keys):

    msg = msg ** keys[1] % keys[2]

    return msg

    
if __name__ == '__main__':

    keys = get_keys()

    option = input('str or file: ')


    if option == 'str':

        string = input()

        encoded = []
        print('encoded: ', end = ''),

        for i in string:
            
            sym = rsa_encode(ord(i), keys)
            encoded.append(sym)
            
            print(chr(sym), end = ''),

        print()
        print('decoded: ', end = ''),
        
        for i in encoded:

            sym = rsa_decode(i, keys)
            print(chr(sym), end = ''),

        print()

    else:
        
        f = open('1.zip', 'rb')
        
        data = b32encode(f.read())
        string = data.decode("ascii")
        
        enc_string = ''

        for i in string:
            encoded = rsa_encode(ord(i), keys)
            enc_string += chr(encoded)


        with open('encoded', 'wb') as f_out:
            dump(enc_string, f_out)

        dec_string = ''
            
        for i in enc_string:
            decoded = rsa_decode(ord(i), keys)
            dec_string += chr(decoded)
        print(dec_string)
        decoded_string = b32decode(dec_string)

        with open('decoded_result.zip', 'wb') as f_res:
            dump(decoded_string, f_res)
        
        f.close()
        f_out.close()
        f_res.close()
        

        

        

        
        
