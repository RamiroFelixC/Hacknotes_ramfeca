## Descripción
Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`. Disassemble [this](https://artifacts.picoctf.net/c/512/debugger0_a).


## Hints
+ gdb is a very good debugger to use for this problem and many others!
+ `main` is actually a recognized symbol that can be used with gdb commands.

## Solución
utilizando gdb
``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Reversing/06-GDB_baby_step_1]
└──╼ $gdb debugger0_a
GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from debugger0_a...
(No debugging symbols found in debugger0_a)
(gdb) 
(gdb) layout asm

 0x1129 <main>                   endbr64                                    │
│   0x112d <main+4>                 push   rbp                                 │
│   0x112e <main+5>                 mov    rbp,rsp                             │
│   0x1131 <main+8>                 mov    DWORD PTR [rbp-0x4],edi             │
│   0x1134 <main+11>                mov    QWORD PTR [rbp-0x10],rsi            │
│   0x1138 <main+15>                mov    eax,0x86342                         │
│   0x113d <main+20>                pop    rbp                                 │
│   0x113e <main+21>                ret 

[3]+  Stopped                 gdb debugger0_a
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Reversing/06-GDB_baby_step_1]
└──╼ $


```

Conversión 0x86342 a decimal

``` 
549698

```


## Flag
```picoCTF{549698}```



## Notas adicionales




## Referencias
+ [conversión](https://www.rapidtables.com/convert/number/hex-to-decimal.html)