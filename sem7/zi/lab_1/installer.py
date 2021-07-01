from misc import encrypt_decrypt, get_addr

from pickle import dump

mac = get_addr()

encrypted_mac = encrypt_decrypt(mac) 

with open("license","wb") as file:
    dump(encrypted_mac, file)

print("license was successfully created")
