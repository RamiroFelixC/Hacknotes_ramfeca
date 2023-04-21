## Description
Download this image and find the flag.
[image](https://artifacts.picoctf.net/c/215/pico.flag.png)

## Hints
+ We know the end sequence of the message will be $t3g0.

## Solution
``` bash 
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/05-St3g0]
└──╼ $ls 
pico.flag.png  St3g0.md
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/05-St3g0]
└──╼ $exiftool pico.flag.png 
ExifTool Version Number         : 12.16
File Name                       : pico.flag.png
Directory                       : .
File Size                       : 13 KiB
File Modification Date/Time     : 2023:03:15 21:15:26-06:00
File Access Date/Time           : 2023:04:21 06:41:02-06:00
File Inode Change Date/Time     : 2023:04:21 06:41:02-06:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 585
Image Height                    : 172
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 585x172
Megapixels                      : 0.101
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/05-St3g0]
└──╼ $binwalk pico.flag.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 585 x 172, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, default compression

┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/05-St3g0]
└──╼ $sudo gem install zsteg
[sudo] password for ramdark: 
Successfully installed zsteg-0.2.13
Parsing documentation for zsteg-0.2.13
Done installing documentation for zsteg after 1 seconds
1 gem installed
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/05-St3g0]
└──╼ $zsteg pico.flag.png 
b1,r,lsb,xy         .. text: "~__B>wV_G@"
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_96ae0ac1}$t3g0"
b1,abgr,lsb,xy      .. text: "E2A5q4E%uSA"
b2,b,lsb,xy         .. text: "AAPAAQTAAA"
b2,b,msb,xy         .. text: "HWUUUUUU"
b3,r,lsb,xy         .. file: gfxboot compiled html help file
b3,b,msb,xy         .. file: StarOffice Gallery theme @\002 H\200\004H\002\004H\200$H\022\004H\200\004\010, 0 objects
b4,r,lsb,xy         .. file: Targa image data (16-273) 65536 x 4097 x 1 +4352 +4369 - 1-bit alpha - right "\021\020\001\001\021\021\001\001\021\021\001"
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: Targa image data - Map 272 x 17 x 16 +257 +272 - 1-bit alpha "\020\001\021\001\021\020\020\001\020\001\020\001"
b4,bgr,lsb,xy       .. file: Targa image data - Map 273 x 272 x 16 +1 +4113 - 1-bit alpha "\020\001\001\001"
b4,rgba,lsb,xy      .. file: Novell LANalyzer capture file
b4,rgba,msb,xy      .. file: Applesoft BASIC program data, first line number 8
b4,abgr,lsb,xy      .. file: Novell LANalyzer capture file
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/05-St3g0]
└──╼ $

```


## Flag
==picoCTF{7h3r3_15_n0_5p00n_96ae0ac1}== 



## Addtional notes


## References
+ [zsteg](https://github.com/zed-0xff/zsteg)

