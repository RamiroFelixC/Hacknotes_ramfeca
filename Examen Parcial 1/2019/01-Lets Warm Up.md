
## Objetivo
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? 

## Hints
Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solución
``` bash
┌─[ramdark@parrot]─[~]
└──╼ $python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x70)
'p'

>>> 


```

## Flag

``` flag: picoCTF{p} ```

## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
| python3 | Ayuda a correr el motor de python|
|chr |es una función de python para convertir el número entero que representa el código Unicode en una cadena que representa un carácter correspondiente|




## Referencias
+ [chr python](https://www.freecodecamp.org/espanol/news/guia-de-funciones-de-python-con-ejemplos/)