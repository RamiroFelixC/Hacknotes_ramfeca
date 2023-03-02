
## Objetivo
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

## Hints
+ This program will only work in the webshell or another Linux computer.
+ To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/fc1d77192c544314efece5dd309092e3/warm
+ Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm
+ -h and --help are the most common arguments to give to programs to get more information from them!
+ Not every program implements help features like -h and --help.


## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $ls
flag  ObedientCat.txt  warm  Waveaflag.txt
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $chmod +x warm
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $./warm 
Hello user! Pass me a -h to learn what I can do!
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_6635aa47}
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $


```

## Flag

``` picoCTF{b1scu1ts_4nd_gr4vy_6635aa47} ```


## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
| chmod | Ayuda a cambiar los permisos a los archivos|
|./ |permite ejecutar un programa|




## Referencias

+ [program download](https://mercury.picoctf.net/static/fc1d77192c544314efece5dd309092e3/warm)