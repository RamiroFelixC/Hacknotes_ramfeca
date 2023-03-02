## Objetivo
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Hints 
+ To view the level3.hash.bin file in the webshell, do: $ bvi level3.hash.bin
+ To exit bvi type :q and press enter.
+ The str_xor function does not need to be reverse engineered for this challenge.

## Solución
``` bash
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $ls
Codebooks.txt  fixme1.txt           level2.flag.txt.enc  PWCrack2.txt
codebook.txt   fixme2.py            level2.py            PWCrack3.txt
code.py        fixme2.txt           level3.flag.txt.enc  runme.py
convertme.py   GlitchCat.txt        level3.hash.bin      runme.txt
Convertme.txt  level1.flag.txt.enc  level3.py
fixme1.py      level1.py            PWCrack1.txt
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $cat level3.py
import hashlib

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

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 level3.py
Please enter correct password for flag: f09e
That password is incorrect
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 level3.py
Please enter correct password for flag: 4dcf
That password is incorrect
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 level3.py
Please enter correct password for flag: 87ab
That password is incorrect
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 level3.py
Please enter correct password for flag: dba8
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}


```


## Flag

```picoCTF{m45h_fl1ng1ng_cd6ed2eb} ```

## Notas adicionales
Existe un hash que tiene todas las posibles contraseñas, se prueba una por una hasta encontrar la correcta, es este caso fue **dba8**

## Referencias

+ [Download level3.py](https://artifacts.picoctf.net/c/24/level3.py)
+ [Download level3.flag.txt.enc](https://artifacts.picoctf.net/c/24/level3.flag.txt.enc)
+ [Download hash level 3](https://artifacts.picoctf.net/c/24/level3.hash.bin) 