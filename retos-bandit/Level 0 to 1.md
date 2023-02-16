## Objetivo
The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.


## Datos de acceso
server: bandit.labs.overthewire.org
User:  bandit0
Password: bandit0


## Solución
``` bash
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit0@bandit:~$ 

```
## Notas adicionales


|Comando | Descripcion |
|------------ | ------------|
|ls | Enlistar archivos|
|cat |  mostrar contenido|
| pwd  | muestra la ruta en la que se esta actualmente |
|whoami| para saber en que usuario estoy|
|ls -la| enlista archivos ocultos y en formato largo||



## Referencias 
