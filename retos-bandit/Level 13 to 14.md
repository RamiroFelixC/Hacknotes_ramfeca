## Objetivo
The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note:** **localhost** is a hostname that refers to the machine you are working on

## Datos de acceso
user -> bandit13

password -> wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

## Solución
``` bash
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost -p 2220
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? Yes
Could not create directory '/home/bandit13/.ssh' (Permission denied).
Failed to add the host to the list of known hosts
'''

bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq



┌─[ramdark@parrot]─[~/Documents]
└──╼ $chmod 600 millave.txt
┌─[ramdark@parrot]─[~/Documents]
└──╼ $ssh -i millave.txt bandit14@bandit.labs.overthewire.org -p 2220
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
bandit14@bandit:~$ 





```
## Notas adicionales

Se copió la llave del usuario 13 se guardo en un archivo de texto y despues se accede a ssh del usuario 14. Para poder acceder con la llave es necesario cambiar los permisos por eso se realiza el chmod 600. 

las llaves se generan con **ssh-keygen** las almacena en un archivo la extensión .pub es la pública.



## Referencias
+ [ssh](https://help.ubuntu.com/community/SSH/OpenSSH/Keys)
