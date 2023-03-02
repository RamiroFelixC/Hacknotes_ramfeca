## Objetivo
Run the runme.py script to get the flag. Download the script with your browser or with wget in the webshell. Download runme.py Python script

## Hints
+ If you have Python on your computer, you can download the script normally and run it. Otherwise, use the wget command in the webshell.
+ To use wget in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
+ Type everything after the dollar sign in the webshell: $ wget , then paste the link after the space after wget and press enter. This will download the script for you in the webshell so you can run it!
+ Finally, to run the script, type everything after the dollar sign and then press enter: $ python3 runme.py You should have the flag now!

## Solución
``` bash
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $ls
runme.py
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> runme.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'runme' is not defined
>>> runme.py
[1]+  Stopped                 python3
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $python3 runme.py
picoCTF{run_s4n1ty_run}
┌─[ramdark@parrot]─[~/Desktop/Examen /Pico 2022]
└──╼ $

```

## Flag
 ```picoCTF{run_s4n1ty_run} ```

## Notas adicionales

con el comando python3 y pasando el argumento el programa en .py permite correr dicho programa

## Referencias
+ [runme.py](https://artifacts.picoctf.net/c/86/runme.py)