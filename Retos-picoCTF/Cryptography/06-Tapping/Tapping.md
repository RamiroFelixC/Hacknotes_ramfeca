## Descripción
Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 21610`.

## Hints
+ What kind of encoding uses dashes and dots?
+ The flag is in the format PICOCTF{}

## Solución

``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography]
└──╼ $nc jupiter.challenges.picoctf.org 21610
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ...-- ----. ----- ..--- ----- .---- ----. ..... .---- ----. } 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography]
└──╼ $nc jupiter.challenges.picoctf.org 21610 | xclip -selection c
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography]
└──╼ $

```


Utilizando cyberchef nos entrega 
```
PICOCTFM0RS3C0D31SFUN3902019519 
```

## Flag
``` picoCTF{M0RS3C0D31SFUN3902019519} ```


## Notas adicionales




## Referencias
+ [Codigo Morse](https://en.wikipedia.org/wiki/Morse_code)
+ [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Line%20feed')&input=Li0tLiAuLiAtLi0uIC0tLSAtLi0uIC0gLi4tLiB7IC0tIC0tLS0tIC4tLiAuLi4gLi4uLS0gLS4tLiAtLS0tLSAtLi4gLi4uLS0gLi0tLS0gLi4uIC4uLS4gLi4tIC0uIC4uLi0tIC0tLS0uIC0tLS0tIC4uLS0tIC0tLS0tIC4tLS0tIC0tLS0uIC4uLi4uIC4tLS0tIC0tLS0uIH0gCg)
