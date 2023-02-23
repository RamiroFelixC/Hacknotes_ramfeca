## Objetivo
The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.

## Datos de acceso
+ user -> bandit18
+ password ->hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

## Solución
``` bash
┌─[✗]─[ramdark@parrot]─[~/Documents]
└──╼ $ssh bandit18@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
...
...
Byebye !
Connection to bandit.labs.overthewire.org closed.'
┌─[ramdark@parrot]─[~/Documents]



└──╼ $ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
┌─[ramdark@parrot]─[~/Documents]
└──╼ $


┌─[✗]─[ramdark@parrot]─[~/Documents]
└──╼ $ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
cat readme
awhqfNnAbc1naukrpqDYcF95h7HoMTrC




```
## Notas adicionales

Se pueden ejecutar comandos antes de ejecutar el bash del servidor, por ello se utiliza el comando cat o bin/bash para leer solo el password


## Referencias
