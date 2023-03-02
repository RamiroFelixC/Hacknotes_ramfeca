
## Objetivo
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

## Hints
+ To view the file in the webshell, do: $ nano level1.py
+ To exit nano, press Ctrl and x and follow the on-screen prompts. 
+ The str_xor function does not need to be reverse engineered for this challenge.



## Solución
``` bash

┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $ls
Codebooks.txt  code.py       Convertme.txt  fixme1.txt  fixme2.txt     level1.flag.txt.enc  PWCrack1.txt  runme.txt
codebook.txt   convertme.py  fixme1.py      fixme2.py   GlitchCat.txt  level1.py            runme.py
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $cat level1.py
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 level1.py
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $



```

## Flag

``` picoCTF{545h_r1ng1ng_56891419} ```


## Notas adicionales
El password nos lo brinda en el codigo fuente, por ello se hace un cat, asi mismo, una vez ejecutado el programa le damos el codigo y nos regresa la flag.

## Referencias

+ [level1.py](https://artifacts.picoctf.net/c/51/level1.py)
+ [level1.flag.txt.enc](https://artifacts.picoctf.net/c/51/level1.flag.txt.enc)