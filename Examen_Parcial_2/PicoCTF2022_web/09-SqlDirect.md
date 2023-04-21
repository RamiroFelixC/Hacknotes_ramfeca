## Description
Connect to this PostgreSQL server and find the flag! 'psql -h saturn.picoctf.net -p 60013 -U postgres pico' 
Password is 'postgres'

## Hints
+ What does a SQL database contain?

## Solution

``` bash
┌─[ramdark@parrot]─[~]
└──╼ $psql -h saturn.picoctf.net -p 60013 -U postgres pico
Password for user postgres: 
psql (13.10 (Debian 13.10-0+deb11u1), server 15.2 (Debian 15.2-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.
pico-# help
Use \? for help or press control-C to clear the input buffer.
pico-# \?
pico-# 
pico-# \c pico
psql (13.10 (Debian 13.10-0+deb11u1), server 15.2 (Debian 15.2-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
You are now connected to database "pico" as user "postgres".
pico-# 


pico-# 
pico-# \l
pico-# \dt
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico-# select * from flags;
ERROR:  syntax error at or near "/?"
LINE 1: /?
        ^
pico=# \select * from flags;
invalid command \select
Try \? for help.
pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)

pico=# 

```


## Flag
==picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}== 



## Addtional notes

\l -> enlista las bases de datos 
\c pico -> informacion del sistema
\dt -> lista de las tablas de la base de datos 



## References
