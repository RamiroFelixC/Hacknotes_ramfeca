# HideToSee

## Objetivo

How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/438/atbash.jpg).

## Hints

*  Download the image and try to extract it.

## Solución

### Solución 1
```
Al momento de descargar la imágen, la subimos a la liga donde sera extraida la información:
Dandonos como resultado krxlXGU{zgyzhs_xizxp_01vy23wu}
```
![[Subir imagen.png]]
```
Después el resultado krxlXGU{zgyzhs_xizxp_01vy23wu} se ingresa a la plataforma de cyberchef donde en recipe sera atbash cipher, mostrandonos la bandera:
```
![[atbash cipher.png]]

## Flag

picoCTF{atbash_crack_01eb23df}

## Notas adicionales

**Atbash** es un método muy común de [cifrado (criptografía)](https://es.wikipedia.org/wiki/Cifrado_(criptograf%C3%ADa) "Cifrado (criptografía)") del [alfabeto hebreo](https://es.wikipedia.org/wiki/Alfabeto_hebreo "Alfabeto hebreo"). Pertenece a la llamada [criptografía clásica](https://es.wikipedia.org/wiki/Historia_de_la_criptograf%C3%ADa "Historia de la criptografía") y es un tipo de [cifrado por sustitución](https://es.wikipedia.org/wiki/Cifrado_por_sustituci%C3%B3n "Cifrado por sustitución"). Se le denomina también método de espejo, pues consiste en sustituir la primera letra ([álef](https://es.wikipedia.org/wiki/%D7%90 "א")) por la última ([tav](https://es.wikipedia.org/wiki/%D7%AA "ת")), la segunda ([bet](https://es.wikipedia.org/wiki/%D7%91 "ב")) por la penúltima ([shin](https://es.wikipedia.org/wiki/%D7%A9 "ש")) y así sucesivamente. Uno de sus usos más célebres se da en el [libro de Jeremías](https://es.wikipedia.org/wiki/Libro_de_Jerem%C3%ADas "Libro de Jeremías"),[1](https://es.wikipedia.org/wiki/Atbash#cite_note-1)​ donde a fin de no nombrar [Babilonia](https://es.wikipedia.org/wiki/Babilonia "Babilonia") (בבל, _Babel_) se utiliza el término, en atbash[Sesac](https://es.wikipedia.org/wiki/Sesac "Sesac") (ששך, _Sheshakh_).

## Referencias

[Steganographic Decoder](https://futureboy.us/stegano/decinput.html)
[Cyberchef](https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()&input=a3J4bFhHVXt6Z3l6aHNfeGl6eHBfMDF2eTIzd3V9)
[Atbash](https://es.wikipedia.org/wiki/Atbash)
