## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

## Hints



## Solución
``` bash

┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/10-sharkonwire2]
└──╼ $python3 script.py 
Matplotlib is building the font cache; this may take a moment.
picoCTF{p1LLf3r3d_data_v1a_st3g0}
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/10-sharkonwire2]
└──╼ $


```

script en python
``` python 
from scapy.all import *

packets = rdpcap('capture.pcap')

flag= ''
for p in packets:
    if UDP in p and p[UDP].dport == 22:
            if p[UDP].sport > 5000:
                    flag += chr(p[UDP].sport-5000)

print(flag)
```



## Flag

``` picoCTF{p1LLf3r3d_data_v1a_st3g0} ```


## Notas adicionales



## Referencias
+ [scrapy](https://scapy.net/)