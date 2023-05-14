## Descripción
I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check... Connect to the program on our server: `nc saturn.picoctf.net 62129` Download the program: [chal.py](https://artifacts.picoctf.net/c/296/chal.py)

## Hints
+ 

## Solución

``` python
from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

pride = "".join(choice(ascii_letters + digits) for _ in range(16))
gluttony = getPrime(128)
greed = getPrime(128)
lust = gluttony * greed
sloth = 65537
envy = inverse(sloth, (gluttony - 1) * (greed - 1))

anger = pow(bytes_to_long(pride.encode()), sloth, lust)

print(f"{anger = }")
print(f"{envy = }")

print("vainglory?")
vainglory = input("> ").strip()

if vainglory == pride:
    print("Conquered!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
else:
    print("Hubris!")


```


``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/05-SRA]
└──╼ $python3 exp.py
[+] Opening connection to saturn.picoctf.net on port 55184: Done
77267707673567187440665775936085436258299018514558526557866705447556688673122
14791781675660329371573019526552583116553662083233458206777157968254499153025
Done
DMk6jDCiLCI7LPKa
b'DMk6jDCiLCI7LPKa\r\n'
b'Conquered!\r\n'
b'picoCTF{7h053_51n5_4r3_n0_m0r3_dd808298}\r\n'
[*] Closed connection to saturn.picoctf.net port 55184
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Crypto/05-SRA]
└──╼ $

```

``` python 
from sage.all import *
from pwn import *
from gmpy2 import is_prime
from string import ascii_letters, digits
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse

r = remote('saturn.picoctf.net', 55184)

def is_printable(text):
    alphabet = ascii_letters + digits
    for i in text:
        if i not in alphabet:
            return False
    return True

e = 65537
r.recvuntil(b'anger = ')
c = int(r.recvline().strip().decode())
r.recvuntil(b'envy = ')
d = int(r.recvline().strip().decode())
r.recvline()
print(c)
print(d)

K = divisors(d*e - 1)
print("Done")

list_prime = []
for k in K:
    pp = ((d*e - 1)//k) + 1

    if is_prime(pp) and int(pp).bit_length() == 128:
        list_prime.append(pp)

list_text = []
for p in list_prime:
    for q in list_prime:
        try:
            if inverse(e, (p - 1) * (q - 1)) == d:
                n = p*q
                list_text.append(long_to_bytes(int(pow(c, d, n))))
        except:
            pass


list_text = set(list_text)

for text in list_text:
    try:
        text = text.decode()
        if is_printable(text):
            print(text)
            r.recvuntil(b'> ')
            r.sendline(text.encode())
            print(r.recvline())
            print(r.recvline())
            print(r.recvline())
            break
    except:
        continue
r.close()
```


## Flag
```picoCTF{7h053_51n5_4r3_n0_m0r3_dd808298}```



## Notas adicionales




## Referencias