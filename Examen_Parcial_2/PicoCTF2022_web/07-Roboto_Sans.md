## Description
The flag is somewhere on this web application not necessarily on the website. Find it. Check [this](http://saturn.picoctf.net:64271/) out.
## Hints


## Solution

robots.txt
``` 
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/

```

Algortimo de base64 con ayuda de cyberchef
```
anMvbXlmaWxlLnR4dA: js/myfile.txt
```

Entrando a la ruta http://saturn.picoctf.net:64271/js/myfile.txt
```
picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}

```

## Flag
==picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}== 



## Addtional notes



## References
+ [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=YW5NdmJYbG1hV3hsTG5SNGRB)
