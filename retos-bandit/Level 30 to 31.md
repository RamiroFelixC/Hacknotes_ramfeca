## Objetivo
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.

## Datos de acceso
+ user -> bandit30
+ password -> xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS


## Solución
``` bash

bandit30@bandit:~$ mkdir /tmp/ram30
bandit30@bandit:~$ cd /tmp/ram30
bandit30@bandit:/tmp/ram30$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/ram30$ ls
repo
bandit30@bandit:/tmp/ram30$ cd repo
bandit30@bandit:/tmp/ram30/repo$ ls
README.md
bandit30@bandit:/tmp/ram30/repo$ cat README.md 
just an epmty file... muahaha
bandit30@bandit:/tmp/ram30/repo$ git log
commit cf552c166d78421e64ddf52f850e680075d216e1 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:13 2023 +0000

    initial commit of README.md
bandit30@bandit:/tmp/ram30/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/ram30/repo$ git tag
secret
bandit30@bandit:/tmp/ram30/repo$ git show secret
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
bandit30@bandit:/tmp/ram30/repo$ 






```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
| git tag | impulsor principal de una etiqueta: creación, modificación y eliminación.|
|git show|permite ver de manera extenduida detalles en objetos de git, como las etiquetas, comentarios, etc|




## Referencias
+ [git show](https://www.atlassian.com/git/tutorials/git-show)
+ [git tag](https://www.atlassian.com/es/git/tutorials/inspecting-a-repository/git-tag)
