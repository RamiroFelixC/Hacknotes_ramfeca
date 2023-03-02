## Objetivo
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.

## Hints
+ Remember the flag format is picoCTF{XXXX}
+ What's a pipe? No not that kind of pipe... This kind

## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $nc jupiter.challenges.picoctf.org 7480|grep pico
picoCTF{digital_plumb3r_06e9d954}
┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $

```

## Flag
``` flag: picoCTF{digital_plumb3r_06e9d954} ```

## Notas adicionales

al conectarse al servidor a traves del puerto 7480, filtramos la salida con un pipe "|"  y utilizando grep.

## Referencias
+ [pipe](http://www.linfo.org/pipes.html)
