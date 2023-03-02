## Objetivo
Can you find the flag in file without running it?

## Hints
[strings](https://linux.die.net/man/1/strings)


## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $strings strings | grep pico
picoCTF{5tRIng5_1T_827aee91}
┌─[ramdark@parrot]─[~/Desktop/Examen /2019]
└──╼ $

```

## Flag

``` flag: picoCTF{5tRIng5_1T_827aee91} ```

## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| strings | se usa para regresar la cadena de strings de un archivo|
|grep | se filtra la salida para evitar muchas cadenas y que muestre la bandera directamente|


## Referencias
+ [strings command](https://www.howtogeek.com/427805/how-to-use-the-strings-command-on-linux/)
+ [strings file](https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings)