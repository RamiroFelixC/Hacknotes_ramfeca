## Objetivo
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: Addadshashanammu.zip

## Hints
+ After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solución
``` bash

┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $ls
 Addadshashanammu.zip   ObedientCat.txt               static.ltdis.x86_64.txt
 flag                   static                        warm
 ltdis.sh              "Staticain'talwaysnoise.txt"   Waveaflag.txt
'Nice netcat.txt'       static.ltdis.strings.txt
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $unzip Addadshashanammu.zip 
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $ls
 Addadshashanammu      'Nice netcat.txt'              static.ltdis.strings.txt
 Addadshashanammu.zip   ObedientCat.txt               static.ltdis.x86_64.txt
 flag                   static                        warm
 ltdis.sh              "Staticain'talwaysnoise.txt"   Waveaflag.txt
┌─[ramdark@parrot]─[~/Desktop/Examen /2021]
└──╼ $cd Addadshashanammu/
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu]
└──╼ $ls
Almurbalarammi
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu]
└──╼ $cd Almurbalarammi/
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi]
└──╼ $ls
Ashalmimilkala
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi]
└──╼ $cd Ashalmimilkala/
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala]
└──╼ $ls
Assurnabitashpi
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala]
└──╼ $cd Assurnabitashpi/
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi]
└──╼ $ls
Maelkashishi
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi]
└──╼ $cd Mae
bash: cd: Mae: No such file or directory
┌─[✗]─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi]
└──╼ $cd Maelkashishi/
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi]
└──╼ $ls
Onnissiralis
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi]
└──╼ $cd Onnissiralis/
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis]
└──╼ $ls
Ularradallaku
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis]
└──╼ $cd Ularradallaku/
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└──╼ $ls
fang-of-haynekhtnamet
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└──╼ $./fang-of-haynekhtnamet 
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_a00cae70}
┌─[ramdark@parrot]─[~/Desktop/Examen /2021/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└──╼ $


```

## Flag

``` flag: picoCTF{l3v3l_up!_t4k3_4_r35t!_a00cae70} ```



## Notas adicionales
se utiliza el comando unzip para poder descomprimir y para navegar entre los directorios cd


## Referencias
+ [unzip](https://www.hostinger.mx/tutoriales/comando-unzip-linux)
+ [file Addadshashanammu.zip ](https://mercury.picoctf.net/static/a350754a299cb58988d6d47aed5be3ba/Addadshashanammu.zip)