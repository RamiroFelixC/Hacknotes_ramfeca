
## Objetivo
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the password is **bandit0**. Once logged in, go to the [Level 1](https://overthewire.org/wargames/bandit/bandit1.html) page to find out how to beat Level 1.


## Datos de acceso
server: bandit.labs.overthewire.org
User:  bandit0
Password: bandit0


## Solución
```
$ssh bandit0@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit0@bandit.labs.overthewire.org's password: 

```
## Notas adicionales

Utilizamos el comando 
*ls* -> para enlistar los archivos
	*ls -la* -> listar archivosen forma extendida
*pwd*  -> conocer en que ruta estoy 

## Referencias 

https://en.wikipedia.org/wiki/Secure_Shell
https://www.wikihow.com/Use-SSH

`