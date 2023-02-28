## Objetivo
There is a git repository at `ssh://bandit27-git@localhost/home/bandit27-git/repo`. The password for the user `bandit27-git` is the same as for the user `bandit27`.

Clone the repository and find the password for the next level.

## Datos de acceso
+ user -> bandit27
+ password -> YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS


## Solución
``` bash
bandit27@bandit:/tmp$ mkdir /tmp/mydir666
bandit27@bandit:/tmp$ cd /tmp/mydir666
bandit27@bandit:/tmp/mydir666$ ls
bandit27@bandit:/tmp/mydir666$ ls -la
total 100
drwxrwxr-x  2 bandit27 bandit27  4096 Feb 24 23:14 .
drwxrwx-wt 24 root     root     98304 Feb 24 23:14 ..
 
bandit27@bandit:/tmp/mydir666$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

bandit27@bandit:/tmp/mydir666$ ls
repo
bandit27@bandit:/tmp/mydir666$ cd repo
bandit27@bandit:/tmp/mydir666/repo$ ls
README
bandit27@bandit:/tmp/mydir666/repo$ cat README 
The password to the next level is: AVanL161y9rsbcJIsFHuw35rjaOM19nR
bandit27@bandit:/tmp/mydir666/repo$ 


```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
| git clone | permite clonar un repositorio  |
|mktemp -d| crea una carpeta temporal|



## Referencias
+ [git commands](https://www.atlassian.com/git/glossary)
