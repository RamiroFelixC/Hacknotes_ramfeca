## Descripción
We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.

## Hints
+ Try fixing the file header


## Solución
``` bash
└──╼ $file mystery 
mystery: data
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/08-C0rrupt]
└──╼ $vim mystery 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/08-C0rrupt]
└──╼ $vim mystery 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/08-C0rrupt]
└──╼ $pngcheck -v mystery 
File: mystery (202941 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
  chunk IDAT at offset 0x00057, length 65445
    zlib: deflated, 32K window, fast compression
  chunk IDAT at offset 0x10008, length 65524
  chunk IDAT at offset 0x20008, length 65524
  chunk IDAT at offset 0x30008, length 6304
  chunk IEND at offset 0x318b4, length 0
  additional data after IEND chunk
ERRORS DETECTED in mystery
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/08-C0rrupt]
└──╼ $open mystery 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/08-C0rrupt]
└──╼ $



```

Editando los encabezados 
```
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
```



## Flag

``` picoCTF{c0rrupt10n_1847995} ```


## Notas adicionales
Editando con vim 
+ vim filename
+ :%!xxd -> para ser mas legible
+ una vez editado -> :%!xxd -r
+ :wq para guardar cambios


## Referencias
+ [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
+ [edit vim](https://transang.me/edit-binary-file-with-vim-and-the-xxd-command/)
