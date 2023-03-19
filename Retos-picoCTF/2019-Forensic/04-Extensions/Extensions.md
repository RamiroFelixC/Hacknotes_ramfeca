## Descripción
This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

## Hints
+ How do operating systems know what kind of file it is? (It's not just the ending!
+ Make sure to submit the flag as picoCTF{XXXXX}

## Solución
``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/04-Extensions]
└──╼ $file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/04-Extensions]
└──╼ $mv flag.txt flag.png
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/04-Extensions]
└──╼ $open flag.png
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/04-Extensions]
└──╼ $


```


## Flag

``` picoCTF{now_you_know_about_extensions} ```


## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| mv | se utiliza para mover archivos y directorios de una ubicación a otra, también es utilizado para renombrar archivos|


## Referencias
+ [File format](https://en.wikipedia.org/wiki/File_format)
+ [List of File Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures/)
