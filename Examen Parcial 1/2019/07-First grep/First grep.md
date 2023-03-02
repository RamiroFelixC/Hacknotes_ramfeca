## Objetivo
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

## Hints
grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solución
``` bash

┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $ls
 2Warm.txt  'First grep.txt'   Strings_it.txt
 Bases.txt   LetsWarmUP.txt    WarmedUp.txt
 file        strings          'what'\''sanetcat?.txt'
┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $grep pico file
picoCTF{grep_is_good_to_find_things_dba08a45}
┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $

```
## Flag

``` flag: picoCTF{grep_is_good_to_find_things_dba08a45} ```

## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| grep | permite buscar en base a una cadena de caracteres|



## Referencias
+ [grep](https://ryanstutorials.net/linuxtutorial/grep.php)
+ [download "file"](https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file)
