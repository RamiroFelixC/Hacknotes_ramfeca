## Descripción
Can you figure out how this program works to get the flag? Connect to the program with netcat: `$ nc saturn.picoctf.net 52057` The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/528/picker-IV.c). The binary can be downloaded [here](https://artifacts.picoctf.net/c/528/picker-IV).

## Hints
+ With Python, there are no binaries. With compiled languages like C, there is source code, and there are binaries. Binaries are created from source code, they are a conversion from the human-readable source code, to the highly efficient machine language, in this case: x86_64.
+ How can you find the address that `win` is at?

## Solución

Dado que el programa pide una dirección y se cuenta con el archivo binario se puede analizar para saber la dirección de la funcion `win`

``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/01-PickerIV]
└──╼ $objdump -d picker-IV

000000000040129e <win>:
  40129e:	f3 0f 1e fa          	endbr64 
  4012a2:	55                   	push   %rbp
  4012a3:	48 89 e5             	mov    %rsp,%rbp
  4012a6:	48 83 ec 10          	sub    $0x10,%rsp
  4012aa:	48 8d 3d 74 0d 00 00 	lea    0xd74(%rip),%rdi        # 402025 <_IO_stdin_used+0x25>
  4012b1:	e8 3a fe ff ff       	call   4010f0 <puts@plt>
  4012b6:	48 8d 35 71 0d 00 00 	lea    0xd71(%rip),%rsi        # 40202e <_IO_stdin_used+0x2e>
  4012bd:	48 8d 3d 6c 0d 00 00 	lea    0xd6c(%rip),%rdi        # 402030 <_IO_stdin_used+0x30>
  4012c4:	e8 87 fe ff ff       	call   401150 <fopen@plt>
  4012c9:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
  4012cd:	48 83 7d f0 00       	cmpq   $0x0,-0x10(%rbp)
  4012d2:	75 16                	jne    4012ea <win+0x4c>
  4012d4:	48 8d 3d 5e 0d 00 00 	lea    0xd5e(%rip),%rdi        # 402039 <_IO_stdin_used+0x39>
  4012db:	e8 10 fe ff ff       	call   4010f0 <puts@plt>
  4012e0:	bf 00 00 00 00       	mov    $0x0,%edi
  4012e5:	e8 86 fe ff ff       	call   401170 <exit@plt>
  4012ea:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  4012ee:	48 89 c7             	mov    %rax,%rdi
  4012f1:	e8 2a fe ff ff       	call   401120 <fgetc@plt>
  4012f6:	88 45 ff             	mov    %al,-0x1(%rbp)
  4012f9:	eb 1a                	jmp    401315 <win+0x77>
  4012fb:	0f be 45 ff          	movsbl -0x1(%rbp),%eax
  4012ff:	89 c7                	mov    %eax,%edi
  401301:	e8 da fd ff ff       	call   4010e0 <putchar@plt>
  401306:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  40130a:	48 89 c7             	mov    %rax,%rdi
  40130d:	e8 0e fe ff ff       	call   401120 <fgetc@plt>
  401312:	88 45 ff             	mov    %al,-0x1(%rbp)
  401315:	80 7d ff ff          	cmpb   $0xff,-0x1(%rbp)
  401319:	75 e0                	jne    4012fb <win+0x5d>
  40131b:	bf 0a 00 00 00       	mov    $0xa,%edi
  401320:	e8 bb fd ff ff       	call   4010e0 <putchar@plt>
  401325:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  401329:	48 89 c7             	mov    %rax,%rdi
  40132c:	e8 cf fd ff ff       	call   401100 <fclose@plt>
  401331:	90                   	nop
  401332:	c9                   	leave  
  401333:	c3                   	ret 
```


``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/01-PickerIV]
└──╼ $nc saturn.picoctf.net 59695
Enter the address in hex to jump to, excluding '0x': 40129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_14bc5444}
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/01-PickerIV]
└──╼ $

```


## Flag
```picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_14bc5444}```



## Notas adicionales




## Referencias

+ [Extracción de información a un binario](https://www.cs.swarthmore.edu/~newhall/unixhelp/binaryfiles.html)
