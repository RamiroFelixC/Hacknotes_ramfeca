## Objetivo
Can you convert the number 42 (base 10) to binary (base 2)? 


## Hints
Submit your answer in our competition's flag format. For example, if your answer was '11111', you would submit 'picoCTF{11111}' as the flag.



## Solución
``` bash

┌─[✗]─[ramdark@parrot]─[~]
└──╼ $python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> bin(42)
'0b101010'
>>> 



```

## Flag

```flag: picoCTF{101010}```
 

## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| bin | permite convertir un numero a binario|



## Referencias
+ [coversion entre bases python](https://www.datacamp.com/tutorial/python-data-type-conversion)