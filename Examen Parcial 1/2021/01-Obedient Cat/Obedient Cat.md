## Objetivo
This file has a flag in plain sight (aka "in-the-clear"). 

## Hints
+ Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
+ To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/a5683698ac318b47bd060cb786859f23/flag
+ $ man cat


## Solución
``` bash
┌─[ramdark@parrot]─[~/Desktop/Examen ]
└──╼ $cd 2021
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $cat flag
picoCTF{s4n1ty_v3r1f13d_4a2b35fd}
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $


```

## Flag 

``` flag: picoCTF{s4n1ty_v3r1f13d_4a2b35fd} ```

## Notas adicionales
Se hace uso del comando cat para visualizar el contenido de un archivo.


## Referencias
+ [download flag](https://mercury.picoctf.net/static/a5683698ac318b47bd060cb786859f23/flag)