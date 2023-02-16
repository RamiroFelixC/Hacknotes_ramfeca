## Objetivo
The password for the next level is stored in the file **data.txt** next to the word **millionth**

## Datos de acceso
user -> bandit7
password -> z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

## Solución
``` bash
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ nano data.txt
Unable to create directory /home/bandit7/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit7@bandit:~$ wc data.txt
  98567  197133 4184396 data.txt
bandit7@bandit:~$ grep millionth data.txt
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
bandit7@bandit:~$ 

  

```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|wc | brinda los datos de la cantidad de lineas, bytes y caracteres|
|grep| filtra la salida para mostrar solo las lineas que coinciden un patron|

tambien se puede utilizar nano, y buscar la palabra especifica

## Referencias