## Descripción
Can you solve this? What two positive numbers can make this possible: `n1 > n1 + n2 OR n2 > n1 + n2` Enter them here `nc saturn.picoctf.net 56201`. [Source](https://artifacts.picoctf.net/c/452/flag.c)


## Hints
+ Integer overflow
+ Not necessarily a math problem


## Solución

``` c
#include <stdio.h>
#include <stdlib.h>

static int addIntOvf(int result, int a, int b) {
    result = a + b;
    if(a > 0 && b > 0 && result < 0)
        return -1;
    if(a < 0 && b < 0 && result > 0)
        return -1;
    return 0;
}

int main() {
    int num1, num2, sum;
    FILE *flag;
    char c;

    printf("n1 > n1 + n2 OR n2 > n1 + n2 \n");
    fflush(stdout);
    printf("What two positive numbers can make this possible: \n");
    fflush(stdout);
    
    if (scanf("%d", &num1) && scanf("%d", &num2)) {
        printf("You entered %d and %d\n", num1, num2);
        fflush(stdout);
        sum = num1 + num2;
        if (addIntOvf(sum, num1, num2) == 0) {
            printf("No overflow\n");
            fflush(stdout);
            exit(0);
        } else if (addIntOvf(sum, num1, num2) == -1) {
            printf("You have an integer overflow\n");
            fflush(stdout);
        }

        if (num1 > 0 || num2 > 0) {
            flag = fopen("flag.txt","r");
            if(flag == NULL){
                printf("flag not found: please run this on the server\n");
                fflush(stdout);
                exit(0);
            }
            char buf[60];
            fgets(buf, 59, flag);
            printf("YOUR FLAG IS: %s\n", buf);
            fflush(stdout);
            exit(0);
        }
    }
    return 0;
}

```


``` bash
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/04-Two-sum]
└──╼ $bc 
bc 1.07.1
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006, 2008, 2012-2017 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'. 
2^31
2147483648
^C
(interrupt) use quit to exit.
^Z
[3]+  Stopped                 bc
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/04-Two-sum]
└──╼ $nc saturn.picoctf.net 56201
n1 > n1 + n2 OR n2 > n1 + n2 
What two positive numbers can make this possible: 
2147483648
47
You entered -2147483648 and 47
No overflow
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/04-Two-sum]
└──╼ $nc saturn.picoctf.net 56201
n1 > n1 + n2 OR n2 > n1 + n2 
What two positive numbers can make this possible: 
2147483647
47
You entered 2147483647 and 47
You have an integer overflow
YOUR FLAG IS: picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_bc0adfd1}

┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Examen_parcial_3/BinaryExplotation/04-Two-sum]
└──╼ $

```


## Flag
```picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_bc0adfd1}```



## Notas adicionales




## Referencias