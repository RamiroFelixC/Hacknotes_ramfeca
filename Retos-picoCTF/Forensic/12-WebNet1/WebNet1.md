## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.

## Hints
+ Try using a tool like Wireshark.
+ How can you decrypt the TLS stream?



## Solución
``` bash

┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/12-WebNet1]
└──╼ $ls
capture.pcap  picopico.key  WebNet1.md
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/12-WebNet1]
└──╼ $whireshark capture.pcap 
bash: whireshark: command not found
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/12-WebNet1]
└──╼ $wireshark capture.pcap 
11:06:47.693     Main Warn FIX Add drag reordering to UAT dialog
11:08:10.098     Main Warn QXcbConnection: XCB error: 3 (BadWindow), sequence: 8525, resource id: 11164373, major code: 40 (TranslateCoords), minor code: 0
^C
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/12-WebNet1]
└──╼ $ssldump -r capture.pcap -k picopico.key -d | grep pico
    61 67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73    ag: picoCTF{this
    67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73 2e    g: picoCTF{this.
    Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
    00 00 00 01 00 00 00 01 70 69 63 6f 43 54 46 7b    ........picoCTF{
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/12-WebNet1]
└──╼ $ssldump -r capture.pcap -k picopico.key -d | grep pico -A 2
    61 67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73    ag: picoCTF{this
    2e 69 73 2e 6e 6f 74 2e 79 6f 75 72 2e 66 6c 61    .is.not.your.fla
    67 2e 61 6e 79 6d 6f 72 65 7d 0d 0a 43 6f 6e 74    g.anymore}..Cont
--
    67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73 2e    g: picoCTF{this.
    69 73 2e 6e 6f 74 2e 79 6f 75 72 2e 66 6c 61 67    is.not.your.flag
    2e 61 6e 79 6d 6f 72 65 7d 0d 0a 43 6f 6e 74 65    .anymore}..Conte
--
    Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
    Keep-Alive: timeout=5, max=99
    Connection: Keep-Alive
--
    00 00 00 01 00 00 00 01 70 69 63 6f 43 54 46 7b    ........picoCTF{
    68 6f 6e 65 79 2e 72 6f 61 73 74 65 64 2e 70 65    honey.roasted.pe
    61 6e 75 74 73 7d 00 00 ff e2 02 1c 49 43 43 5f    anuts}......ICC_
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/12-WebNet1]
└──╼ $



```


## Flag
``` picoCTF{honey.roasted.peanuts} ```


## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
| ssldump | Se utiliza para rastrear una conexión TCP|
|-r |para pasar la captura|
|-k |para pasar la key de ssl|



## Referencias
+ [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)