## pentesterlab.com From Blind SQL Injection to Shell II in python

I rewrote the script from https://pentesterlab.com/exercises/from_sqli_to_shell_II/course
in python. 

The injetion is a blind, time-based, X-Forwarded-For header injection. 

The algorithm used could be MASSIVELY optimized. It is basically worst-case 
right now. 

This algorithm is currently limited by the value of index setting on line 64.

So, it will only return whatever the value is minus 1, so if the index is 10, 
it'll return 9 tables. 

Additionally, the script will need to be manually stopped when enumerating the user, version, and admin
password. 

Updates are coming. 
