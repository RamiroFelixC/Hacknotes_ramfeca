## Description
Now you DON’T see me. This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
## Hints
+ How can you be sure of the redaction?

## Solution
``` bash 
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/04-Redaction_gone_wrong]
└──╼ $ls 
 Financial_Report_for_ABC_Labs.pdf  'Redaction gone wrong.md'
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/04-Redaction_gone_wrong]
└──╼ $open Financial_Report_for_ABC_Labs.pdf 
┌─[ramdark@parrot]─[~/Desktop/Examen2/picoCTF2022_Forensics/04-Redaction_gone_wrong]
└──╼ $

```
Contenido del pdf 
``` 
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.
Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.

```


## Flag
==picoCTF{C4n_Y0u_S33_m3_fully}== 



## Addtional notes


## References
