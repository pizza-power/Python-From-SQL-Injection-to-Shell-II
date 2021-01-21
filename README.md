## pentesterlab.com From Blind SQL Injection to Shell II in python

I rewrote the script from https://pentesterlab.com/exercises/from_sqli_to_shell_II/course
in python. 

The injetion is a blind, time-based, X-Forwarded-For header injection. 

If I get around to it, I'll update it with an option to enumerate tables,users, etc. This version
just gives you the admin name and password.

Additionally, the injection could be optimized to reduced requests drastically.  
