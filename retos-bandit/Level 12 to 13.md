## Objetivo
The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Datos de acceso
user -> bandit12

password -> JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

## Solución
``` bash
bandit12@bandit:~$ xxd -r data.txt | file -
/dev/stdin: gzip compressed data, was "data2.bin", last modified: Wed Jan 11 19:18:38 2023, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat |file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |file -
/dev/stdin: gzip compressed data, was "data4.bin", last modified: Wed Jan 11 19:18:38 2023, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |zcat |file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |zcat|tar xo |file -
tar: data5.bin: Cannot open: Permission denied
tar: Exiting with failure status due to previous errors
/dev/stdin: empty
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |zcat|tar xO |file -
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |zcat|tar xO |tar xO|bzcat|tar xO|zcat|file -
/dev/stdin: ASCII text
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |zcat|tar xO |tar xO|bzcat|tar xO|zcat
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
bandit12@bandit:~$ 


```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|xxd | permite hacer un vaciado hexadecimal o incluso hacer lo contrario|
|-r|tansforma de hexadecimal a binario| 
|zcat| permite ver el contenido de un archivo comprimido sin descomprimirlo|
|bzcat|descromprime todos los archivos especificados|
|tar |es usado para comprimir o empaquetar un archivo o directorio|
|xO||


	Algunos tipos de compresion en Linux  
-----------------------------------------------------  
	ext     comp     desc                       ver en consola  
	-----------------------------------------------------  
	.gz     gzip      gzip -d (gunzip)          zcat  
	.bz2   bzip2    bzip2 -d (bunzip2)     bzcat  
	.tar      tar t      ar xf                            tar xO  
	----------------------------------------------------  
	otros (instalar) :  
	.zip zip unzip (7z x)  
	.rar rar unrar (7z x)

## Referencias
+ [bzcat](https://www.commandlinux.com/man-page/man1/bzcat.1.html)
+ [zcat](https://es.linux-console.net/?p=2219#gsc.tab=0)
+ [Hex dump]("https://en.wikipedia.org/wiki/Hex_dump")
