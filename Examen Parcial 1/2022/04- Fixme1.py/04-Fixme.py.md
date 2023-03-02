## Objetivo
Fix the syntax error in this Python script to print the flag. 

## Hints
+ Indentation is very meaningful in Python
+ To view the file in the webshell, do: $ nano fixme1.py
+ To exit nano, press Ctrl and x and follow the on-screen prompts.
+ The str_xor function does not need to be reverse engineered for this challenge.


## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $ls
Codebooks.txt  code.py       Convertme.txt  fixme1.txt  runme.txt
codebook.txt   convertme.py  fixme1.py      runme.py
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 fixme1.py
  File "/home/ramdark/Desktop/Examen /Pico 2022/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $cat fixme1.py

import random



def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) + chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) + chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x5e) + chr(0x52) + chr(0x0c) + chr(0x01) + chr(0x42) + chr(0x57) + chr(0x59) + chr(0x0a) + chr(0x14)

  
flag = str_xor(flag_enc, 'enkidu')
  print('That is correct! Here\'s your flag: ' + flag)

┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $nano fixme1.py

  GNU nano 5.4                                               fixme1.py *                                                I      
import random



def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x0>

  
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)

                                    [ line 20/22 (90%), col 1/53 (1%), char 781/835 (93%) ]
^H Help        ^O Read File   ^R Replace     ^V Paste       ^G Go To Line  ^Y Redo        M-6 Copy       ^Q Where Was
^X Exit        ^F Where Is    ^K Cut         ^T Execute     ^Z Undo        M-A Set Mark   M-] To Bracket M-Q Previous


┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $

```

## Flag
```picoCTF{1nd3nt1ty_cr1515_09ee727a} ```

## Notas adicionales

Se corrige la linea 20 del programa, en este caso la identación estaba incorrecta

## Referencias
+ [Download "fixme1.py"](https://artifacts.picoctf.net/c/38/fixme1.py)