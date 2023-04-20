## Descripción
We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with `nc jupiter.challenges.picoctf.org 43522`.

## Hints
+ Flag is not in the usual flag format


## Solución

``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography]
└──╼ $nc jupiter.challenges.picoctf.org 43522
-------------------------------------------------------------------------------
mjfysqnr uasa gr zjvs tlqy - tsaovafmz_gr_m_jcas_lqwikq_jytwqvfsqt
-------------------------------------------------------------------------------
da dasa fjn wvmu wjsa nuqf q ovqsnas jt qf ujvs jvn jt jvs rugp ngll da rqd uas rgfb, qfk nuaf g vfkasrnjjk tjs nua tgsrn ngwa duqn dqr waqfn iz q rugp tjvfkasgfy gf nua raq.  g wvrn qmbfjdlakya g uqk uqsklz azar nj ljjb vp duaf nua raqwaf njlk wa rua dqr rgfbgfy; tjs tsjw nua wjwafn nuqn nuaz sqnuas pvn wa gfnj nua ijqn nuqf nuqn g wgyun ia rqgk nj yj gf, wz uaqsn dqr, qr gn dasa, kaqk dgnugf wa, pqsnlz dgnu tsgyun, pqsnlz dgnu ujssjs jt wgfk, qfk nua nujvyunr jt duqn dqr zan iatjsa wa.
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography]
└──╼ $


```


Utilizando substitution solver  nos entrega 
```
-------------------------------------------------------------------------------
congrats here is your flag - frequency_is_c_over_lambda_ogfmaunraf
-------------------------------------------------------------------------------
we were not much more than a quarter of an hour out of our ship till we saw her sink, and then i understood for the first time what was meant by a ship foundering in the sea.  i must acknowledge i had hardly eyes to look up when the seamen told me she was sinking; for from the moment that they rather put me into the boat than that i might be said to go in, my heart was, as it were, dead within me, partly with fright, partly with horror of mind, and the thoughts of what was yet before me.

```

## Flag
``` frequency_is_c_over_lambda_ogfmaunraf ```


## Notas adicionales




## Referencias
+ [Substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher)
+ [Substitution solver](https://www.guballa.de/substitution-solver)}
