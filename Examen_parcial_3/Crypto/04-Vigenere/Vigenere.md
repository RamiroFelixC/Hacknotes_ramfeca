## Descripción
Can you decrypt this message? Decrypt this [message](https://artifacts.picoctf.net/c/158/cipher.txt) using this key "CYLAB".

## Hints
+ https://en.wikipedia.org/wiki/Vigen%C3%A8re_ciphe

## Solución

Utilizando ciberchef decodificamos el mensaje obteniendo la bandera 

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/04-Vigenere]
└──╼ $
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/04-Vigenere]
└──╼ $ls 
cipher.txt  Vigenere.md
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/04-Vigenere]
└──╼ $cat cipher.txt 
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/04-Vigenere]

```


## Flag
```picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}```



## Notas adicionales




## Referencias
+ [Vigenere](https://en.wikipedia.org/wiki/Vigen%C3%A8re_ciphe)
+ [Solver](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('CYLAB')&input=cmdub0RWRHtPME5VX1dRM19HMUczTzNUM19BMUFIM1NfY2M4MjI3MmJ9Cg)
