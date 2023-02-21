## Objetivo
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

## Datos de acceso
user -> bandit9
password -> EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## Solución
``` bash
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ file data.txt
data.txt: data
bandit9@bandit:~$ strings data.txt | grep ==
c========== the
h;========== password
========== isT
n.E========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit9@bandit:~$  


  

```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|strings | sustrae la cadena de texto de un archivo data, solo deja los caracteres que se pueden mostrar|


## Referencias