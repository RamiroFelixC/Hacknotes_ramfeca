## Objetivo
Fix the syntax error in the Python script to print the flag. 

## Hints
+ Are equality and assignment the same symbol?
+ To view the file in the webshell, do: $ nano fixme2.py
+ To exit nano, press Ctrl and x and follow the on-screen prompts.
+ The str_xor function does not need to be reverse engineered for this challenge.


## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $ls
Codebooks.txt  code.py       Convertme.txt  fixme1.txt  fixme2.txt  runme.txt
codebook.txt   convertme.py  fixme1.py      fixme2.py   runme.py
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 fixme2.py
  File "/home/ramdark/Desktop/Examen /Pico 2022/fixme2.py", line 22
    if flag = "":
            ^
SyntaxError: invalid syntax


┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $nano fixme2.py 

  GNU nano 5.4                                               fixme2.py                                                  I      
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x58) + chr(0x1>

  
flag = str_xor(flag_enc, 'enkidu')

# Check that flag is not empty
if flag == "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)

                                  [ line 26/28 (92%), col 1/1 (100%), char 1028/1030 (99%) ]
^H Help        ^O Read File   ^R Replace     ^V Paste       ^G Go To Line  ^Y Redo        M-6 Copy       ^Q Where Was
^X Exit        ^F Where Is    ^K Cut         ^T Execute     ^Z Undo        M-A Set Mark   M-] To Bracket M-Q Previous


...


┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $



```

## Flag
``` picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc} ```

## Notas adicionales

Se corrige la linea 22 del programa, en este caso, dado que se realiza una condicion se necesita "==" y no "="

## Referencias
+ [Download "fixme2.py"](https://artifacts.picoctf.net/c/38/fixme1.py)