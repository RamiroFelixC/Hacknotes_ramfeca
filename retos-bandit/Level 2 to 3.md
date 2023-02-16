## Objetivo
The password for the next level is stored in a file called **spaces in this filename** located in the home directory


## Datos de acceso
user -> bandit2
password -> rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

## Solución
``` bash
bandit2@bandit:~$ whoami
bandit2
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename" 
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit2@bandit:~$ 
  

```
## Notas adicionales
Cuando se quiere leer el contenido de un archivo que esta nombreado con esapacios se puede leer incluyendo comillas " " o utilizando barras invertidas.  


## Referencias 
+ [archivos nombrados con espacios](https://linuxhandbook.com/filename-spaces-linux/) 
