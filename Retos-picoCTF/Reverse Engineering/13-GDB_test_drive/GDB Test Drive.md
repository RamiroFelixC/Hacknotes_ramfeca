## Objetivo

Can you get the flag? Download this [binary](https://artifacts.picoctf.net/c/87/gdbme). Here's the test drive instructions:

-   `$ chmod +x gdbme`
-   `$ gdb gdbme`
-   `(gdb) layout asm`
-   `(gdb) break *(main+99)`
-   `(gdb) run`
-   `(gdb) jump *(main+104)`
## Hints

## Solución

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/13-GDB_test_drive]
└──╼ $file gdbme 
gdbme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=15cc42b7d1ba7d200593c720e2d9fd2e757fccca, for GNU/Linux 3.2.0, not stripped
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/13-GDB_test_drive]
└──╼ $chmod +x gdbme 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/13-GDB_test_drive]
└──╼ $
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Reverse Engineering/13-GDB_test_drive]
└──╼ $gdb gdbme
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
Reading symbols from gdbme...
(No debugging symbols found in gdbme)
(gdb) 

Breakpoint 1, 0x000055555555532a in main ()
(gdb) jump *(main+104)
Continuing at 0x55555555532f.
picoCTF{d3bugg3r_dr1v3_7776d758}
[Inferior 1 (process 5566) exited normally]
(gdb) 




```

## Flag

picoCTF{d3bugg3r_dr1v3_7776d758}

## Notas adicionales


## Referencias