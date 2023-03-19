## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.

## Hints
+ Try using a tool like Wireshark
+ What are streams?

## Solución
``` 
Utilizando wireshark como examinador de paquetes, se analizan los paquetes del protocolo UDP, meidante el follow en steam. Ahi en el paquete 6 se puede apreciar la bandera. 


```


## Flag

``` picoCTF{StaT31355_636f6e6e} ```


## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| exiftool | herramienta para leer, escribir y manipular metadatos de imágenes, audio, video y PDF.|


## Referencias
+ [pcap](https://www.comparitech.com/net-admin/pcap-guide/)
