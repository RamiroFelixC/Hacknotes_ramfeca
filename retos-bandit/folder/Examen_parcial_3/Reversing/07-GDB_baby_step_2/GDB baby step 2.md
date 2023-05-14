## Descripción
Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`. Debug [this](https://artifacts.picoctf.net/c/520/debugger0_b).


## Hints
+ You could calculate `eax` yourself, or you could set a breakpoint for after the calculcation and inspect `eax` to let the program do the heavy-lifting for you.

## Solución


``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Reversing/07-GDB_baby_step_2]
└──╼ $chmod +x debugger0_b 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Reversing/07-GDB_baby_step_2]
└──╼ $gdb debugger0_b
Reading symbols from debugger0_b...
(No debugging symbols found in debugger0_b)
(gdb) layout asm

0x401106 <main>         endbr64                                            
0x40110a <main+4>       push   rbp                                         
0x40110b <main+5>       mov    rbp,rsp                                     
0x40110e <main+8>       mov    DWORD PTR [rbp-0x14],edi                    
0x401111 <main+11>      mov    QWORD PTR [rbp-0x20],rsi                    
0x401115 <main+15>      mov    DWORD PTR [rbp-0x4],0x1e0da                 
0x40111c <main+22>      mov    DWORD PTR [rbp-0xc],0x25f                   
0x401123 <main+29>      mov    DWORD PTR [rbp-0x8],0x0                     
0x40112a <main+36>      jmp    0x401136 <main+48>                          
0x40112c <main+38>      mov    eax,DWORD PTR [rbp-0x8]                     
0x40112f <main+41>      add    DWORD PTR [rbp-0x4],eax                     
0x401132 <main+44>      add    DWORD PTR [rbp-0x8],0x1                     
0x401136 <main+48>      mov    eax,DWORD PTR [rbp-0x8]
0x401139 <main+51>      cmp    eax,DWORD PTR [rbp-0xc]             
0x40113c <main+54>      jl     0x40112c <main+38>                  
0x40113e <main+56>      mov    eax,DWORD PTR [rbp-0x4]             
0x401141 <main+59>      pop    rbp                                 
0x401142 <main+60>      ret

(gdb) break *(main+59)
Breakpoint 1 at 0x401141
(gdb) run
Starting program: /home/ramdark/Documents/Hacking_Notes_RFC/Examen_parcial_3/Reversing/07-GDB_baby_st
ep_2/debugger0_b

Breakpoint 1, 0x0000000000401141 in main ()
(gdb) info registers eax 
eax            0x4af4b             307019
(gdb) 




[6]+  Stopped                 gdb debugger0_b
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/Reversing/07-GDB_baby_step_2]
└──╼ $



```


## Flag
```picoCTF{307019}```



## Notas adicionales




## Referencias
+ [registers in gdb](https://stackoverflow.com/questions/5429137/how-to-print-register-values-in-gdb)