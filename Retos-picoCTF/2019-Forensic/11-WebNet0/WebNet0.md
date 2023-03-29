## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag..

## Hints
+ Try using a tool like Wireshark.
+ How can you decrypt the TLS stream?



## Solución
``` bash

┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/11-WebNet0]
└──╼ $ssldump -r capture.pcap -k picopico.key -d | grep pico
    61 67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67    ag: picoCTF{nong
    67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67 73    g: picoCTF{nongs
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/11-WebNet0]
└──╼ $ssldump -r capture.pcap -k picopico.key -d | grep pico -A 2
    61 67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67    ag: picoCTF{nong
    73 68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63    shim.shrimp.crac
    6b 65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c    kers}..Content-L
--
    67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67 73    g: picoCTF{nongs
    68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63 6b    him.shrimp.crack
    65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65    ers}..Content-Le
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/11-WebNet0]
└──╼ $


```


## Flag
``` picoCTF{nongshim.shrimp.crackers} ```


## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
| ssldump | Se utiliza para rastrear una conexión TCP|
|-r |para pasar la captura|
|-k |para pasar la key de ssl|



## Referencias
+ [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)