## Descripción
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/75e646e4ad19967ca1811f895fb40465/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/75e646e4ad19967ca1811f895fb40465/scrambled2.png)

## Hints
+ Think of different ways you can "stack" images


## Solución

``` bash
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/11-Pixelated]
└──╼ $python3 exploit.py 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/11-Pixelated]
└──╼ $ls
exploit.py  flag.png  pixelated.md  scrambled1.png  scrambled2.png
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/11-Pixelated]
└──╼ $open flag.png 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/Cryptography/11-Pixelated]
└──╼ $

```

```python
from PIL import Image
import numpy as np

img1 = np.asarray(Image.open('scrambled1.png'))
img2 = np.asarray(Image.open('scrambled2.png'))

datos = img1.copy()+img2.copy()
nueva = Image.fromarray(datos)

nueva.save('flag.png','PNG')
```

## Flag
``` picoCTF{d562333d} ```


## Notas adicionales




## Referencias
+ [Visual Cryptography]([https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
+ [stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)
