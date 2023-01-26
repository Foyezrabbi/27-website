import requests
from bs4 import BeautifulSoup

import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

i = 1
file_name = "gifa.com"
with open(f"{file_name}.email.txt", "w"):
    pass

with open(f"{file_name}.txt", "r") as files:
    for url in files.readlines():
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        email_list = re.findall(r'email":"(.*?)"', str(soup))
        email = ''
        if len(email_list) != 0:
            email = email_list[0]

        print(f"{i} {email=}")
        with open(f"{file_name}.email.txt", 'a') as file:
            file.write(f"{email}\n")
            i += 1
print("done")
