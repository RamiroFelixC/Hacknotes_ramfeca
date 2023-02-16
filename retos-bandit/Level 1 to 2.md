## Objetivo
The password for the next level is stored in a file called **-** located in the home directory


## Datos de acceso
bandit1
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

## Solución
``` bash
bandit1@bandit:~$ whoami
bandit1
bandit1@bandit:~$ pwd
/home/bandit1
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$  

```
## Notas adicionales
Cuando se quiere leer el contenido de un archivo que esta definido con un - al inicio se puede leer utilizando el cat con "./-" o utilizando cat /home/bandit1/


## Referencias 

 [archivos nombrados con "-" al inicio](https://stackoverflow.com/questions/42187323/how-to-open-a-dashed-filename-using-terminal)
 
 
 

