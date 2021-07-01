from misc import encrypt_decrypt, get_addr

from pickle import load

from pathlib import Path


file = Path("license")

if file.is_file():

    try:
        with open("license","rb") as file:
            temp = load(file)
        temp = encrypt_decrypt(temp)

        mac = get_addr()

        if mac == temp:
            print("have fun!")
            
        else:
            print("license codes doesnt match:(")

    except Exception:
        print("license file is corrupted")

else:
    print("no license file")


