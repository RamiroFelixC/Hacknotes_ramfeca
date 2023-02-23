## Objetivo
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think

## Datos de acceso
+ user -> bandit20
+ password -> VxCazJaVykI6W36BkBU0mJTCM8rR95XT


## Solución
``` bash
bandit20@bandit:~$ nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 1557216
bandit20@bandit:~$ Listening on 0.0.0.0 2020

bandit20@bandit:~$ ./suconnect 2020
Connection received on 127.0.0.1 34384
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
bandit20@bandit:~$ ^C
[1]+  Done                    nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$ 





```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|nc -lnvp | abre el puerto (l -> listen, p -> puerto, n-> no resolucion de nombres, v-> mostrar una salida) |
|&| permite enviar un proceso a segundo plano|
|jobs|permite ver el estado de los procesos en los puertos|


## Referencias

