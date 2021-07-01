from Crypto.Signature import pkcs1_15
from pickle import load
from os.path import isfile
from Crypto.PublicKey.RSA import generate, import_key

from main import get_hash


if __name__ == '__main__':

    f_name = input('input filename: ')

    if isfile('key') & isfile('signature') & isfile(f_name):

        f_key = open('key', 'r')

        with open('signature', 'rb') as f_sign:
            signature = load(f_sign)
        
        key = import_key(f_key.read())

        hash = get_hash(f_name)

        f_key.close()

        try:
            pkcs1_15.new(key).verify(hash, signature)
            print('all good')
            
        except ValueError:
            print('elec signatures dnt match')

    else:
        print('not enough')

        
