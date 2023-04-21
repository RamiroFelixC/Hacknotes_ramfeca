
## Descripción
Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png).

## Hints
+ What does meta mean in the context of files?
+ Ever heard of metadata?

## Solución
``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/02-So Meta]
└──╼ $ls
'So Meta.md'
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/02-So Meta]
└──╼ $wget https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png
--2023-03-17 11:18:44--  https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 108795 (106K) [application/octet-stream]
Saving to: ‘pico_img.png’

pico_img.png        100%[===================>] 106.25K  --.-KB/s    in 0.1s    

2023-03-17 11:18:45 (742 KB/s) - ‘pico_img.png’ saved [108795/108795]

┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/02-So Meta]
└──╼ $ls
 pico_img.png  'So Meta.md'
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/02-So Meta]
└──╼ $exiftool pico_img.png 
ExifTool Version Number         : 12.16
File Name                       : pico_img.png
Directory                       : .
File Size                       : 106 KiB
File Modification Date/Time     : 2020:10:26 12:38:23-06:00
File Access Date/Time           : 2023:03:17 11:18:45-06:00
File Inode Change Date/Time     : 2023:03:17 11:18:45-06:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_fec06741}
Image Size                      : 600x600
Megapixels                      : 0.360
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/02-So Meta]
└──╼ $


```


## Flag

``` picoCTF{s0_m3ta_fec06741} ```


## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| exiftool | herramienta para leer, escribir y manipular metadatos de imágenes, audio, video y PDF.|


## Referencias
+ [Metadata](https://en.wikipedia.org/wiki/Metadata)