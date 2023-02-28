## Objetivo
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not **/bin/bash**, but something else. Find out what it is, how it works and how to break out of it.

## Datos de acceso
+ user -> bandit25
+ password -> p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d


## Solución
``` bash

bandit25@bandit:~$ 
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
bandit25@bandit:~$


Found a swap file by the name "/tmp/text.txt.swp"
          owned by: bandit26   dated: Tue Feb 21 23:09:29 2023
         file name: ~bandit26/text.txt
          modified: YES
         user name: bandit26   host name: bandit
        process ID: 101955
While opening file "text.txt"
             dated: Tue Feb 21 22:03:08 2023
  _                     _ _ _   ___   __
r: /etc/bandit_pass/bandit26
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
~                                                                         
~                                                                         
<etc/bandit_pass/bandit26





```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|more |muestra el texto por partes y permite editar un archivo mediante vi |
|vi|editor de texto|
|:q| salir de vi|
|:r| ejecutar un comando|
|:e| editar|
|:qa!| forzar la salida|



Se juega con el tamaño de la consola para poder hacer que aparezca "more" una ves ahi con "v" entramos a vim para poder ejecutar comandos en este caso se hizo el 
"r: /etc/bandit_pass/bandit26"  para poder leer el password del usuario 26.

## Referencias