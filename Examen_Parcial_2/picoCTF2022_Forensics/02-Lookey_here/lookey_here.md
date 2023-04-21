## Description
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data [here](https://artifacts.picoctf.net/c/124/anthem.flag.txt).
## Hints
+ Download the file and search for the flag based on the known prefix.

## Solution


``` bash 

┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/02-Lookey_here]
└──╼ $cat anthem.flag.txt 

....
<the enslaved, and my home will become the capital of a world
      where each man will be free to exist for his own sake.

      For the coming of that day shall I fight, I and my sons and my
      chosen friends. For the freedom of Man. For his rights. For his
      life. For his honor.

      And here, over the portals of my fort, I shall cut in the stone
      the word which is to be my beacon and my banner. The word which
      will not die, should we all perish in battle. The word which can
      never die on this earth, for it is the heart of it and the
      meaning and the glory.

      The sacred word:

      EGO



┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/02-Lookey_here]
└──╼ $cat anthem.flag.txt | grep picoCTF
      we think that the men of picoCTF{gr3p_15_@w3s0m3_4c479940}
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/02-Lookey_here]
└──╼ $

```

## Flag
==picoCTF{gr3p_15_@w3s0m3_4c479940}== 



## Addtional notes


## References

