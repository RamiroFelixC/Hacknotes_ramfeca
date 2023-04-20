## Descripción
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this). Can you reverse the flag.

## Hints
+ objdump and Gihdra are some tools that could assist with this

## Solución

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/10-reverse_cipher]
└──╼ $ls
rev  reverse_cipher.md  rev_this
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/10-reverse_cipher]
└──╼ $cat rev_this
picoCTF{w1{1wq85jc=2i0<}┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/10-reverse_cipher]
└──╼ $python3 exp.py
picoCTF{w1{1wq85jc=2i0<}
r3v3rs37ee84d27
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/10-reverse_cipher]
└──╼ $


```


``` python
cifrado=open('rev_this', 'r').read()
print(cifrado)

flag = ''

for i in range (8, len(cifrado)-1):
    if i & 1 == 0:
        flag += chr(ord(cifrado[i])-5)
    else:
        flag += chr(ord(cifrado[i])+2)
        
print(flag)
```




## Flag
``` picoCTF{r3v3rs37ee84d27} ```


## Notas adicionales




## Referencias
+ [x64 assembly](https://www.intel.com/content/dam/develop/external/us/en/documents/introduction-to-x64-assembly-181178.pdf)
+ [ghidra](https://ghidra-sre.org/)
+ [ida-pro](https://hex-rays.com/ida-pro/)