# HideToSee

## Objetivo

How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/438/atbash.jpg).

## Hints

*  Download the image and try to extract it.

## Solución

``` bash
┌──[ramdark@parrot]─[~/Desktop]
└──╼ $cd ..
┌─[ramdark@parrot]─[~]
└──╼ $cd Desktop/
┌─[ramdark@parrot]─[~/Desktop]
└──╼ $steghide extract -sf atbash.jpg 
Enter passphrase: 
wrote extracted data to "encrypted.txt".
┌─[ramdark@parrot]─[~/Desktop]
└──╼ $cat encrypted.txt 
krxlXGU{zgyzhs_xizxp_8z0uvwwx}
┌─[ramdark@parrot]─[~/Desktop]
└──╼ $

```

## Flag

picoCTF{atbash_crack_8a0feddc}

## Notas adicionales


## Referencias

[Steganographic Decoder](https://futureboy.us/stegano/decinput.html)
[Cyberchef](https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()&input=a3J4bFhHVXt6Z3l6aHNfeGl6eHBfMDF2eTIzd3V9)
[Atbash](https://es.wikipedia.org/wiki/Atbash)
