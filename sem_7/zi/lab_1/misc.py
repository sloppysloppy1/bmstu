from uuid import getnode as get_mac


def encrypt_decrypt(addr):

    key = 5
    temp = []

    for i in range (len(addr)):
        num = addr[i] ^ key
        temp.append(num)

    return temp


def get_addr():
    
    temp = get_mac()
    
    mac = list(map(int, str(temp)))

    return mac

