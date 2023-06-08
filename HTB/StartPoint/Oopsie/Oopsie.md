utilizando burpsuite nos damos cuenta que el sript de login se encuetra en /cdn-cgi/login

ahora con las cookies se observa que cambiando el valor de guest a admin el id a 1 nos da la cuenta del administrador

|   |   |   |
|---|---|---|
|34322|admin|admin@megacorp|


With what kind of tool can intercept web traffic?
proxy

What is the path to the directory on the webserver that returns a login page?
/cdn-cgi/login

What can be modified in Firefox to get access to the upload page?
cookie

What is the access ID of the admin user?
34322

On uploading a file, what directory does that file appear in on the server?
/uploads

What is the file that contains the password that is shared with the robert user?
db.php

What executible is run with the option "-group bugtracker" to identify all files owned by the bugtracker group?
find

Regardless of which user starts running the bugtracker executable, what's user privileges will use to run?
root

What SUID stands for?
set owner user id

What is the name of the executable being called in an insecure manner?
cat

Submit user flag
f2c74ee8db7983851ab2a96a44eb7981

Submit root flag
af13b0bee69f8a877c3faf667f7beacf