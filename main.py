import requests
from bs4 import BeautifulSoup
import string

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

i = 1
alphabet = list(string.ascii_lowercase)
file_name = "gifa.com"
link = "https://www.gifa.com"

for j in alphabet:
    url = f"https://www.boot.com/vis/v1/en/directory/{j}?oid=58808&lang=2"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for tag in soup.find_all('div', class_='exh-table-col exh-table-col--name'):
        for a in tag.find_all('a'):
            name_url = a.get('href')  # for getting link

            print(a.text)  # for getting text between the link
            print(f"{i} {name_url = }")
            text = f"{name_url}\n".split("#")[0]
            with open(f"{file_name}.txt", 'a+') as file:
                file.write(f"{link}{text}")
                i += 1

print("done")
