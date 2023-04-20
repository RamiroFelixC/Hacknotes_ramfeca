## Descripción
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext).

## Hints
+ caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

## Solución

``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/04-Caesar]
└──╼ $ls 
Caesar.md  ciphertext
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/04-Caesar]
└──╼ $cat ciphertext 
picoCTF{dspttjohuifsvcjdpoabrkttds}┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/04-Caesar]
└──╼ $python3 script.py 
crossingtherubiconzaqjsscr
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/04-Caesar]
└──╼ $

```

```python
import string 
import re

abc=string.ascii_letters

encryp = open('ciphertext','r').read()
encryp = re.findall('\{(.*?)\}', encryp)[0]

rot = 25
salida = ''
for car in encryp:
    salida+= abc[(abc.find(car)+rot)%26]

print(salida)
```

## Flag
``` picoCTF{crossingtherubiconzaqjsscr} ```


## Notas adicionales




## Referencias
+ [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)