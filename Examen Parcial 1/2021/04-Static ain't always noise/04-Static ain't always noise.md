## Objetivo
Can you look at the data in this binary: static? This BASH script might help!


## Solución
``` bash

┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $ls -la
total 44
drwxr-xr-x 1 ramdark ramdark   130 feb 28 06:54  .
drwxr-xr-x 1 ramdark ramdark    34 feb 28 04:49  ..
-rw-r--r-- 1 ramdark ramdark    34 feb 28 06:39  flag
-rw-r--r-- 1 ramdark ramdark   785 feb 28 06:54  ltdis.sh
-rw-r--r-- 1 ramdark ramdark   718 feb 28 06:52 'Nice netcat.txt'
-rw-r--r-- 1 ramdark ramdark   408 feb 28 06:42  ObedientCat.txt
-rw-r--r-- 1 ramdark ramdark  8376 feb 28 06:54  static
-rwxr-xr-x 1 ramdark ramdark 10936 feb 28 06:43  warm
-rw-r--r-- 1 ramdark ramdark   942 feb 28 06:47  Waveaflag.txt
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $./ltdis.sh
bash: ./ltdis.sh: Permission denied
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $chmod +x ltdis.sh
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $./ltdis.sh
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $cat static.ltdis.strings.txt|grep pico
   1020 picoCTF{d15a5m_t34s3r_ae0b3ef2}
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $


```
## Flag

``` picoCTF{d15a5m_t34s3r_ae0b3ef2} ```



## Notas adicionales

Se hace uso de comandos como chmod +x para permitir ejecutar el archivo. Y para ejecuartlo se pasa como argumento el archivo static, la salida se vacia en un txt llamado "static.ltdis.strings.txt". 



## Referencias

+ [static download](https://mercury.picoctf.net/static/e9dd71b5d11023873b8abe99cdb45551/static)
+ [ltdis.sh download](https://mercury.picoctf.net/static/e9dd71b5d11023873b8abe99cdb45551/ltdis.sh)
