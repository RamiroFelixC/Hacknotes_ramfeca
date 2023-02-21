## Objetivo
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

## Datos de acceso
user -> bandit10
password -> G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

## Solución
``` bash
bandit10@bandit:~$ whoami
bandit10
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ echo "Hello"
Hello
bandit10@bandit:~$ echo "Hello" | base64
SGVsbG8K
bandit10@bandit:~$ echo -n SGVsbG8K | base64 -d
Hello
bandit10@bandit:~$ base64 -d data.txt
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ echo "VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==" | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ python
>>> import base64
>>>base64.b64decode('VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==')
b'The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM\n'
>>>
bandit10@bandit:~$ 

```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|echo | imprime un texto en pantalla de la terminal|
|echo -n|interruptor que omite el nuevo caracter de linea| 
|base64| es un decodificador/codificador utilizando la bae 64|
|base64 -d|se usa para decodificar cualquier dato codiicado de una entrada estandar|
|python|corre los scripts de phyton|
|base64.b64decode|script de python que permite decodificar datos en base 64|

también se puede utilizar cyberchef 
## Referencias
+ [base64](https://linuxhint.com/bash_base64_encode_decode/)
+ [echo](https://tecnonautas.net/como-dar-salida-a-texto-en-la-pantalla-usando-el-comando-linux-echo/)
+ [cyberchef]([CyberChef](https://gchq.github.io/CyberChef/))
+ 