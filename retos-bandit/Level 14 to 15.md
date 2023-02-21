## Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.

## Datos de acceso
user -> bandit14

password -> fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

## Solución
``` bash
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

^C
bandit14@bandit:~$ 



```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|netcat **nc** | permite conectarse a un puerto|




## Referencias
+ [ip address](http://computer.howstuffworks.com/web-server5.htm)
+ [localhost](https://en.wikipedia.org/wiki/Localhost)
