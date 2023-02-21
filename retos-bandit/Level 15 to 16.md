## Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

**Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…**

## Datos de acceso
user -> bandit15

password ->jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

## Solución
``` bash
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 20 08:54:11 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 20 08:54:11 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 20 08:53:11 2023 GMT; NotAfter: Feb 20 08:54:11 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEISBn8DANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwMjIwMDg1MzExWhcNMjMwMjIwMDg1NDExWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDA
N2o6Mg1ffDxuv9nKKhQ7D0aYSNwkuZnUkOfkpz2ejbLBYABhVOCosUFXY4dQ/Wrf
VJ+wwloNVzOoNh5aMyVw2K/dCDzvaYEVSpXHzOmM5B8widqzB4lMrG1MxO2Q4u5g
T5wxU7IUhbXJbtqoRETiP9PLGRMap9FtAHujTCxqZmsvyhqGEL25dbQ256I+oN6T
wmmzZFYAptTPAx2oZkSGGLKx/nwCu05W27eqrlQ4D3PdDg1/tTjc2Z4KL03pYn7T
Aax+qZp9ufBGE8hrF33Lrv0XOQx94JYM2WWmey3HAzPBMWlifAYpr+GlRVONmll/
awAU4bckc09ffC2QHPhTAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQAk
BTv9GO6xdo+mVEp8lv8otcXAlJcqTUmwOd9FdEVBPp2eOwB5U1iTt59W/fG4GoBD
Q6plqgxOzguF+Y1lWz5x1FheIfq7kXdIrQMPjxN99btTXimEmPm4S0HJYEcUfeog
d3Wg5CLY9UUAubZLLhqv1vp/T6KFgV63Bz0yLCTdIGRaO4goE1C6s4FkMRBcnyPm
ezrLPiZJxJ2963bS7tAMFK7BryL9N2IiwMh/uF7uGSTSdJ4ngIfJ/HFZzOPtx+yx
5XHJHV3KUsNoKKTl6oIJCcgozOZPCk4wmDq/FutZ89wWoncd4EAqXageyK7FvjNM
42TH1Z+5M8CkB4aQThxv
-----END CERTIFICATE-----
---
'''
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
bandit15@bandit:~$ 




```
## Notas adicionales
|Comando | Descripcion |
|------------ | ------------|
|nmap | hace un escaneo de puertos abiertos por default escanea los primeros 1000 |
|open ssl| permite comunicarse bajo el protocolo ssl bajo el parametro cliente, conexión y el puerto|



## Referencias
+ [Open ssl](https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html)
+ [SSL](https://en.wikipedia.org/wiki/Secure_Socket_Layer)
