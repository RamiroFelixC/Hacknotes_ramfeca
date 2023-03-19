## Descripción
Decode this [message](https://jupiter.challenges.picoctf.org/static/d6fcea5e3c6433680ea4f914e24fab61/message.wav) from the moon.

## Hints
+ How did pictures from the moon landing get sent back to Earth?
+ What is the CMU mascot?, that might help select a RX option


## Solución
``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/06-m00nwalk]
└──╼ $file message.wav 
message.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/06-m00nwalk]
└──╼ $sstv -d message.wav -o flag.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [##############################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/06-m00nwalk]
└──╼ $ls
flag.png  m00nwalk.md  message.wav
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/Retos-picoCTF/2019-Forensic/06-m00nwalk]
└──╼ $




```


## Flag

``` picoCTF{beep_boop_im_in_space} ```


## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| sstv | permite decodificar videos en imagenes|



## Referencias
+ [Apollo 11](https://en.wikipedia.org/wiki/Apollo_11_missing_tapes)
+ [SSTV decoder](https://github.com/colaclanth/sstv)