import requests
from bs4 import BeautifulSoup
import urllib.parse
all_data = []

for i in range(1,19):
    print(f'getting page {i}')
    url = f'https://www.yellowpages.ca/search/si/{i}/Indian+Restaurant/Mississauga+ON'
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    #cards = soup.select('div.listing > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')
    cards = soup.select('.mlr__item__cta')
    for card in cards:
        try:
            link = card.get('href')
        except:
            pass
        if link is not None:
            if 'redirect' in link:
                link = link.split('=')
                link = link[1]
                dlink = urllib.parse.unquote(link)
                all_data.append(dlink)

with open(r'links.txt', 'w') as fp:
    for item in all_data:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')