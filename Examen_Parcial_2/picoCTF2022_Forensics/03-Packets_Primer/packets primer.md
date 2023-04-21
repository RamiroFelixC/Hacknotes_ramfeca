## Description
Download the packet capture file and use packet analysis software to find the flag.
[Download packet capture](https://artifacts.picoctf.net/c/194/network-dump.flag.pcap)
## Hints
+ Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.

## Solution


``` 
Ayudandonos de wireshark inspeccionamos los paquetes, por lo cual nos damos cuenta de que se utiliza el protocolo TCP simplemente damos click boton derecho y vamos a "follow" -> "TCP steam" y en un paquete aparece la bandera. 

```


![[packets_primer_img.png]]


## Flag
==picoCTF{p4ck37_5h4rk_ceccaa7f}== 



## Addtional notes


## References
