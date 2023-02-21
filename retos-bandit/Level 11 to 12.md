## Objetivo
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Datos de acceso
user -> bandit11

password -> 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

## Solución
``` bash
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit11@bandit:~$ 


bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ python3
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import codecs
>>> codecs.decode('Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi','rot13')
'The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv'
>>> 


```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|tr | permite traducir: cambiar caracteres, buscar palabras, eliminar caracteres, añadir una linea, etc desde la entrada estandar|
|python3|corre los scripts de phyton| 
|codecs.decode| modulo para decodicar recibe como parametros la cadena de caracteres y la función a realizar|
|rot13|funcion en python que nos ayuda a decifrar el algoritmo rot13|

formato para tr

tr     Opciones     conjunto_caracteres_1 conjunto_caracteres_2

Donde:

`tr`: Parte del comando que hace que se ejecute la utilidad tr.

`Opciones`: Se puede dejar en blanco o usar las opciones `-c`, `-d`, `-s`, y `-t`. 

`conjunto_caracteres_1`: Conjunto de caracteres que se buscaran en un texto.

`conjunto_caracteres_2`: Conjunto de caracteres que se usarán para modificar un texto

## Referencias
+ [tr](https://geekland.eu/uso-del-comando-tr-en-linux-y-unix-con-ejemplos/)
+ [rot13](https://en.wikipedia.org/wiki/Rot13)
