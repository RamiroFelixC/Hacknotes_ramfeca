## Descripción
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/bf5e2c8811afb4669f4a6850e097e8aa/values)

## Hints
+ Bits are expensive, I used only a little bit over 100 to save money


## Solución

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/12-Mind_your_Ps_and_Qs]
└──╼ $ls
'Mind your Ps and Qs.md'   values
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/12-Mind_your_Ps_and_Qs]
└──╼ $cat values 
Decrypt my super sick RSA:
c: 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n: 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e: 65537┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/12-Mind_your_Ps_and_Qs]
└──╼ $python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from Crypto.Util.number import long_to_bytes
>>> from Crypto.Util.number import inverse
>>> c=421345306292040663864066688931456845278496274597031632020995583473619804626233684
>>> e=65537
>>> p=1461849912200000206276283741896701133693
>>> q=431899300006243611356963607089521499045809
>>> n=p*q
>>> tn=(p-1)*(q-1)
>>> d=inverse(e,tn)
>>> m=pow(c,d,n)
>>> long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_55304594}'
>>> 


```



## Flag
``` picoCTF{sma11_N_n0_g0od_55304594} ```


## Notas adicionales




## Referencias
+ [Factordb](http://factordb.com/)
+ [RsaCtftool](https://github.com/RsaCtfTool/RsaCtfTool)
+ 