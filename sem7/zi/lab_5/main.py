from Crypto.Hash import SHA512
from Crypto.PublicKey.RSA import generate, import_key
from Crypto.Signature import pkcs1_15
from os import urandom
from os.path import isfile
from pickle import dump


def get_hash(file):
    
    hash = SHA512.new()

    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            
            hash.update(chunk)

    return hash


def get_private_key():

    private_key = generate(1024, urandom)

    return private_key


def get_public_key(key):

    publ_key = open('key', 'wb')
    
    public_key = key.publickey()
    publ_key.write(public_key.export_key('PEM'))

    publ_key.close()

    
def get_signature(hash, key):

    signature = pkcs1_15.new(key).sign(hash)

    return signature


if __name__ == '__main__':

    f_name = input('input filename: ')
    
    hash = get_hash(f_name)

    key = get_private_key()
    
    signature = get_signature(hash, key)

    get_public_key(key)
    
    with open('signature','wb') as f_sign:
        dump(signature, f_sign)

    print('sent')
    

    
    
