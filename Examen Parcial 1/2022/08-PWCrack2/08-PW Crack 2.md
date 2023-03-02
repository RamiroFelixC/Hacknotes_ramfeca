## Objetivo
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

## Hints 
+ Does that encoding look familiar?
+ The str_xor function does not need to be reverse engineered for this challenge.

## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $ls
Codebooks.txt  fixme1.py      level1.flag.txt.enc  PWCrack2.txt
codebook.txt   fixme1.txt     level1.py            runme.py
code.py        fixme2.py      level2.flag.txt.enc  runme.txt
convertme.py   fixme2.txt     level2.py
Convertme.txt  GlitchCat.txt  PWCrack1.txt
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $cat level2.py
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

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))
4ec9
>>> 
[3]+  Stopped                 python3
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 level2.py
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $



```

## Flag
```picoCTF{tr45h_51ng1ng_9701e681} ```


## Notas adicionales
El password nos lo brinda en el codigo fuente en codigo ascii (hacemos la conversion con python), por ello se hace un cat, asi mismo, una vez ejecutado el programa le damos el codigo y nos regresa la flag.

## Referencias

+ [download level2.py](https://artifacts.picoctf.net/c/17/level2.py)
+ [ download level2.flag.txt.enc](https://artifacts.picoctf.net/c/17/level2.flag.txt.enc)