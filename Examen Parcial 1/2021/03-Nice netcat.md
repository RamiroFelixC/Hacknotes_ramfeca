## Objetivo
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 49039, but it doesn't speak English...

## Hints
+ You can practice using netcat with this picoGym problem: what's a netcat?
+ You can practice reading and writing ASCII with this picoGym problem: Let's Warm Up

## Solución
``` bash

┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $nc mercury.picoctf.net 49039
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
51 
100 
56 
52 
101 
100 
99 
56 
125 
10 
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $


```

## Flag

``` picoCTF{g00d_k1tty!_n1c3_k1tty!_3d84edc8} ```

## Notas adicionales
Cada valor decimal se convierte a su respectivo ascii.


## Referencias
+ [conversion de decimal a ascii](https://onlineasciitools.com/convert-decimal-to-ascii)