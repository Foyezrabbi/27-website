import requests
from bs4 import BeautifulSoup
import string
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
alphabet = list(string.ascii_lowercase)
alphabet.append("other")

url_dict = {
    0: {
        "url": "https://www.boot.com/vis/v1/en/directory/f?oid=58808&lang=2",
    },
    1: {
        "url": "https://www.euroshop-tradefair.com/vis/v1/en/directory/e?oid=18864&lang=2"
    },

    2: {
        "url": "https://www.prowein.com/vis/v1/en/directory/f?oid=29558&lang=2"
    },

    3: {
        "url": "https://www.beauty-duesseldorf.com/vis/v1/en/directory/other?oid=42770&lang=2"
    },
    4: {
        "url": "https://www.top-hair-international.com/vis/v1/en/directory/d?oid=11920&lang=2"
    },
    5: {
        "url": "https://www.thermprocess.de/vis/v1/de/directory/other?oid=290392&lang=1"
    },
    6: {
        "url": "https://www.caravan-salon.com/vis/v1/en/directory/other?oid=6884&lang=2"
    },
    7: {
        "url": "https://www.rehacare.com/vis/v1/en/directory/n?oid=43612&lang=2"

    },
    8: {
        "url": "https://www.aplusa-online.com/vis/v1/en/directory/o?oid=19008&lang=2"

    },
    9: {
        "url": "https://www.medica-tradefair.com/vis/v1/en/directory/m?oid=80398&lang=2"

    },
    10: {
        "url": "https://www.decarbxpo.com/vis/v1/en/directory/k?oid=6468&lang=2"

    },
    11: {
        "url": "https://www.eurocis-tradefair.com/vis/v1/en/directory/o?oid=49779&lang=2"

    },
    12: {
        "url": "https://www.tube-tradefair.com/vis/v1/en/directory/p?oid=2370196&lang=2"

    },
    13: {
        "url": "https://www.valveworldexpo.com/vis/v1/en/directory/p?oid=8560&lang=2"

    },
    14: {
        "url": "https://www.k-online.com/vis/v1/en/directory/q?oid=87922&lang=2"

    }
}

for i in range(15):
    file_name1 = url_dict.get(i).get("url")
    file_name2 = str(file_name1)[8:]
    file_name = file_name2.split("/vis/")[0]

    link = f"https://{file_name}"

    first1 = url_dict.get(i).get("url")
    first2 = str(first1).split("directory/")[0]
    first = f"{first2}directory/"

    url_id1 = str(first1).split("directory/")[-1]
    url_id2 = url_id1.split("oid=")[-1]
    url_id = f"?oid={url_id2}"

    i = 0
    for j in alphabet:
        try:
            url = f"{first}{j}{url_id}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            for tag in soup.find_all('div', class_='exh-table-col exh-table-col--name'):
                for a in tag.find_all('a'):
                    name_url = a.get('href')  # for getting link
                    text = f"{name_url}\n".split("#")[0]
                    print(f"{i} {text = }")
                    with open(f"{file_name}.txt", 'a') as file:
                        file.write(f"{link}{text}")
                        i += 1
        except Exception as e:
            print(e)

    i = 0
    try:
        with open(f"{file_name}.txt", "r+") as files:
            for url in files.readlines():
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')

                email_list = re.findall(r'email":"(.*?)"', str(soup))
                email = ''
                if len(email_list) != 0:
                    email = email_list[0]

                print(f"{i} {email = }")
                with open(f"{file_name}.email.txt", 'a+') as file:
                    file.write(f"{email}\n")
                    i += 1

    except Exception as e:
        print(e)
    print("done")
