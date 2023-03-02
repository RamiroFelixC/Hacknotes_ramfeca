## Objetivo
Our flag printing service has started glitching! $ nc saturn.picoctf.net 53933

## Hints
+ ASCII is one of the most common encodings used in programming
+ We know that the glitch output is valid Python, somehow!
+ Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $nc saturn.picoctf.net 53933
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print ('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}')
picoCTF{gl17ch_m3_n07_a4392d2e}
>>> 

```

## Flag

``` picoCTF{gl17ch_m3_n07_a4392d2e} ```


## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| chr | funcion en python que recibiendo un entero proporciona un caracter|

## Referencias

+ [chr python](https://parzibyte.me/blog/2018/12/10/ord-chr-python/)