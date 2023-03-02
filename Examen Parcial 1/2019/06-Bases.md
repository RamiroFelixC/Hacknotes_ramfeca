## Objetivo
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

## Hints

Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
l3arn_th3_r0p35┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $^C
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $

```

## Flag

``` flag: picoCTF{l3arn_th3_r0p35} ```


## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| base64 -d | se usa para codificar y decodificar una base 64|




## Referencias
+ [base64](https://en.wikipedia.org/wiki/Base64)