## Descripción
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message [here](https://artifacts.picoctf.net/c/193/message.txt).


## Hints
+ Split the message up into blocks of 3 and see how the first block is scrambled

## Solución

Utilizando un reparador de transposición fragmentamos el mensaje en bloque de 3 y luego se ordena para que pueda leerse mejor el mensaje obteniendo 
``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/03-transposition-trial]
└──╼ $ls
 message.txt  'Transposition trial.md'
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/03-transposition-trial]
└──╼ $cat message.txt 
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/03-transposition-trial]
```

``` 
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}
```


## Flag
```picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}```



## Notas adicionales




## Referencias
+ [Transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher)
+ [solver](https://tholman.com/other/transposition/)
