## Description
The developer of this website mistakenly left an important artifact in the website source, can you find it? The [website](http://saturn.picoctf.net:52523/) is here

## Hints
+ How could you mirror the website on your local machine so you could use more powerful tools for searching?


## Solution
Al inspeccionar el elemento y analizando cada una de las hojas de estilo en cascada en el css "style.css" en la linea 328 podeos apreciar la bandera en el codigo.


``` css
...

/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49} **/
 .carousel-indicators li {
     width: 20px;
     height: 20px;
     border-radius: 11px;
     background-color: #070000;
}
 .carousel-indicators li.active {
    background-color: #35a30a;
}
 .carousel-indicators {
     left: inherit;
     top: 53%;
     width: 20px;
     display: block;
}
 .carousel-indicators li {
     margin: 8px 0;
}
 .banner_main {
     position: relative;
}

...

```


## Flag
==picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49}== 



## Addtional notes




## References
