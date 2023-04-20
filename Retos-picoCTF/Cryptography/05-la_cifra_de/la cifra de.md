## Descripción
I found this cipher in an old book. Can you figure out what it says? Connect with `nc jupiter.challenges.picoctf.org 32411`.

## Hints
+ There are tools that make this easy.
+ Perhaps looking at history will help

## Solución

``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/04-Caesar]
└──╼ $nc jupiter.challenges.picoctf.org 32411
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x7g996649}

Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.

Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.

Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.

Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.


┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/04-Caesar]
└──╼ $


```

Resultado del ataque de fuerza bruta 
```
Result

Cleartext using the keyword "flag":
```

Utilizando el algoritmo vigenere
```
in 1553 by Giovan Battista Bellaso in his book La cifra del. Sig. Giovan Battista Bellaso 

For the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoCTF{b311a50_0r_v1gn3r3_c1ph3r7b996649}

The first well-documented description of a polyalphabetic cipher however, was made around 1467 by Leon Battista Alberti.

The VigenÃ¨re Cipher is therefore sometimes called the Alberti Disc or Alberti Cipher.

In 1508, Johannes Trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the VigenÃ¨re Cipher.

Bellasoâs second booklet appeared in 1555 as a continuation of the first. The lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.
```


## Flag
``` picoCTF{b311a50_0r_v1gn3r3_c1ph3r7b996649} ```


## Notas adicionales




## Referencias
+ [ataque a la llave](https://www.guballa.de/vigenere-solver)
+ [decodificacion ](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('flag')&input=RW5jcnlwdGVkIG1lc3NhZ2U6Ck5lIGl5IG55dGt3cHN6bnlnIG50aCBpdCBtdHN6dGN5IHZqenByaiB6ZnpqeSBya2hwaWJqIG5ya2l0dCBsdGMgdG5ueWd5IHlzZWUgaXRkIHR0ZSBjeGpsdGsKCklmcm9zciB0bmogbm9hd2RlIHVrIHNpeXl6cmUsIHlzZSBCbnJldMOod3AgQ291c2V4IG1scyBoanBuIHhqdG5ianl0a2kgeGF0ZCBlaXNqZAoKSXogYmxzIGxmd3NrcWogYXp5Y2loemVlaiB5eiBCcmZ0c2sgaXAgVm9scG7DqHhqIGxzIG95IGhheSB0Y2ltbnlhcnFqIGRreG5yb2dwZCBvcyAxNTUzIG15IE1uenZncyBNYXp5dHN6ZiBNZXJxbHN1IG55IGhveCBtb3VwIFdhIGlucXJnIGlwbC4gWW5yLiBHb3RnYXQgR2x0em5kdGcgR3BscmZkbyAKCkx0YyB0bmogdG12cXBta3NlYXpuem4gdWsgZWhveCBuaXZtcHIgZyB5bGJyaiB0cyBsdGNta2kgbXkgeXF0ZG9zciB0bmogd29jamMgaGdxcSBvbCBmeSBveGl0bmd3aiBhcnVzYWhqZSBmdXcgbG4gZ3VhYXhqeXRyZCBjYXRpem0gdHp4Ymt3IHpmIHZxbGNreCBoaXptIGNleXVwY3ogeXogdG5qIGZwdmpjIGhncXFwb2h6Q1pLe20zMTFhNTBfMHhfYTFybjN4M19oMWFoM3g3Zzk5NjY0OX0KCkVoayBrdHJ5eSBoZXJxLW9vaXp4ZXR5cGQgampkY3huYXRvdHkgb2wgZiBhb3JkbGx2bWxia3l0YyBpbmFoa3cgc29jamdleCwgYmxzIHNmb2UgZ3d6dXRpIDE0NjcgbXkgUmp6biBIZmV0b3hlYSBHcW1leHl0LgoKVG5qIEdpbWp5w6hyayBIdHBuamMgaXkgeXNleGpxb3hqIGRvc2plaXNqZCBjZ3F3ZWogeXNlIEdxbWV4eXQgRG94biBveCBGd2Jrd2VpIEluYWhrdy4KClRuIDE1MDgsIFB0c2F0c3BzIFp3dHRuanhpYXggdG5ianl0a2kgZWhrIHh6LWNncXdlaiB5bGJhcWwgcmtoZWEgKGcgcmx0eG5pIG9sIHhzaWx5cGQgZ3FhaGdncHR5KSB5c2F6IGJ6dXJpIHdhempjIGJrIGYgbnJveXRjZ3Egbm9zdXpua3NlIG9sIHlzZSBCbnJldMOod3AgQ291c2V4LgoKR3BscmZkb%2BKAmXkgeHBjdXNvIGJ1dHZsa3kgbHB2amxya2kgdG4gMTU1NSBneCBsIGN1c2VpdHpsdG90eSBvbCB5c2UgbG5jc3ouIFlzZSBydGhleCBtbGxiamQgb2wgeXNlIGdxYWhnZ3B0eSBmY2UgdHRoIHNubnF0a2kgY2VtendheHFqLCBiYXkgZWhrIGZ3cG5mbWV6eCBsbmogeXNlIG9zb2VkIHFwdHpqY3MgZ3dwIG1vY3BkIGhkIHhlZ3NkIG9sIGYgeG5rcnpub2ggdmVlIHVzcmd4cCwgd25ubmggaWZ5IGJrIGl0ZmxqY2V0eSBoaXptIHBhaW0gbm94d3BzdnR5ZGtzZS4)
+ 