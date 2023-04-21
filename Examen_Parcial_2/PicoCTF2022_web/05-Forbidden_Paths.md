## Description
Can you get the flag? Here's the [website](http://saturn.picoctf.net:52278/). We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?

## Hints


## Solution

``` 
dado que flag.txt vive en una ruta especifica y la cual no se tiene acceso autorizado, acomodados la peticion de manera que permita buscar en todo el sistema y en todas las carpetas del directorio actual , es decir, utilizando la ruta "/usr/share/nginx/html/" pero, de manera: ../../../../../ 

```


## Flag
== picoCTF{7h3_p47h_70_5ucc355_6db46514}== 



## Addtional notes




## References
