## Objetivo
The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

-   human-readable
-   1033 bytes in size
-   not executable


## Datos de acceso
user -> bandit5
password -> lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

## Solución
``` bash
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
bandit5@bandit:~/inhere$ find . -readable -size 1033c -type f
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
  

```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|find | busca un archivo|
|-readable|archivos legibles|
|-size| especifica el tamaño|
|-type |especifica el tipo de archivo|
|ls -R|enlista de manera recursiva |

comandos para manuales
man find 
h- muestra la ayuda estando dentro del manual de ayuda
/ readable - busca la palabra readable
N - busca la siguiente ocurrencia hacia atras 
n - busca la ocurrencia hacia adelante 
q - salir del manual de ayuda

## Referencias 