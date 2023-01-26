import requests
from bs4 import BeautifulSoup
import urllib.parse
import pandas as pd

def get_data(num):
    lst = []
    url = f'https://www.yellowpages.ca/search/si/{num}/Indian+Restaurant/Mississauga+ON'
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    cards = soup.select('.listing_right_section')
    for card in cards:
        name = card.select_one('.listing__name > a').get_text()
        city = card.select_one('.listing__address--full > span:nth-child(2)').get_text()
        try:
            y_phone = card.select_one('ul.mlr > li.mlr__item--phone > a').get('data-phone')
        except:
            y_phone = ''
        try:
            link = card.select_one('ul.mlr > li.mlr__item--website > a').get('href')
            link = link.rstrip()
            link = link.split('=')
            link = link[1]
            link = urllib.parse.unquote(link)
        except:
            link = ''
        lst.append({'Name' :name,
                    'City' :city,
                    'Phone' :y_phone,
                    'Website' :link})
    return lst


all_data = []
for pge in range(1,19):
    print(f'getting {pge}')
    ls = get_data(pge)
    for i in ls:
        all_data.append(i)

df = pd.DataFrame(all_data)
df.to_excel('yellowpages.xlsx')