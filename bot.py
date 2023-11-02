import requests
from bs4 import BeautifulSoup

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

url = 'https://smart-lab.ru/q/etf'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find_all('table')
for tr in table:
    td = tr.find_all('tr')
    for f in td:
        td_price = f.find_all('td')
        if (len(td_price)) != 0 and 'EQMX' in td_price[2].text:
            print(td_price[7].text)
