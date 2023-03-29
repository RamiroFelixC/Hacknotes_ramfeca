## Descripción
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/c00c449c3b08daaccacca6f9d5c55d49/Forensics is fun.pptm)
## Hints
...

## Solución
``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/15-Macrohard_Weakedge]
└──╼ $ls
'[Content_Types].xml'  'Forensics is fun.pptm'   ppt
 docProps              'MacroHard WeakEdge.md'   _rels
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/15-Macrohard_Weakedge]
└──╼ $


```

Utilizando un explorador de archivos se observa una cadena de texto en el archivo hidden
```
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q

```

Modificando la cadena
``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/15-Macrohard_Weakedge]
└──╼ $echo "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q" | tr -d " "
ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/15-Macrohard_Weakedge]
└──╼ $echo "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q" | tr -d " " | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/15-Macrohard_Weakedge]
└──╼ $



```


## Flag
``` picoCTF{D1d_u_kn0w_ppts_r_z1p5} ```


## Notas adicionales

tr -d " " -> permite eliminar los espacios de una cadena 



## Referencias
+ [.pptm](https://www.reviversoft.com/es/file-extensions/pptm)
