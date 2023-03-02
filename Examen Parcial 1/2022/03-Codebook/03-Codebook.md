## Objetivo
Run the Python script code.py in the same directory as codebook.txt.

    Download code.py
    Download codebook.txt

## Hints
+ On the webshell, use ls to see if both files are in the directory you are in
+ The str_xor function does not need to be reverse engineered for this challenge. 


## Solución
``` bash
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $ls
Codebooks.txt  code.py       Convertme.txt  runme.txt
codebook.txt   convertme.py  runme.py
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $cat code.py

import random
import sys



def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x13) + chr(0x01) + chr(0x17) + chr(0x07) + chr(0x2c) + chr(0x3a) + chr(0x2f) + chr(0x1a) + chr(0x0d) + chr(0x53) + chr(0x0c) + chr(0x47) + chr(0x0a) + chr(0x5f) + chr(0x5e) + chr(0x02) + chr(0x3e) + chr(0x5a) + chr(0x56) + chr(0x5d) + chr(0x45) + chr(0x5d) + chr(0x58) + chr(0x31) + chr(0x5e) + chr(0x05) + chr(0x5f) + chr(0x53) + chr(0x5a) + chr(0x10) + chr(0x5f) + chr(0x0e) + chr(0x13)



def print_flag():
  try:
    codebook = open('codebook.txt', 'r').read()
    
    password = codebook[4] + codebook[14] + codebook[13] + codebook[14] +\
               codebook[23]+ codebook[25] + codebook[16] + codebook[0]  +\
               codebook[25]
               
    flag = str_xor(flag_enc, password)
    print(flag)
  except FileNotFoundError:
    print('Couldn\'t find codebook.txt. Did you download that file into the same directory as this script?')



def main():
  print_flag()



if __name__ == "__main__":
  main()

┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $cat codebook.txt
azbycxdwevfugthsirjqkplomn
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 code.py 
picoCTF{c0d3b00k_455157_7d102d7a}
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $

```


## Flag
``` picoCTF{c0d3b00k_455157_7d102d7a} ```

## Notas adicionales

El programa en python lo que realiza es imprmir la flag utilizando el archivo .txt

## Referencias
+ [Download code.py](https://artifacts.picoctf.net/c/101/code.py)
+ [Download codebook.txt](https://artifacts.picoctf.net/c/101/codebook.txt) 