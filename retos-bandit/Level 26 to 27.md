## Objetivo
Good job getting a shell! Now hurry and grab the password for bandit27!

## Datos de acceso
+ user -> bandit26
+ password -> c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1


## Solución
``` bash
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
:set shell=/bin/bash

:shell
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
bandit26@bandit:~$ 







```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|:set |establece una variable |
|:|ejecutar un comando en vi|
|./|ejecutar archivos|

Se utiliza vi para ejecutar comandos se establece con set la variable shell como /bin/bash posteriormente se tiene acceso ya a la terminal con el usuario bandit26 

bandit27-do un binario que permite ejecutar comandos a nombre del usuario bandit27, por ello se manda el cat /etc/bandit_pass/bandit27



## Referencias


