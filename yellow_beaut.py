import requests
from bs4 import BeautifulSoup
import urllib.parse
all_data = []

def get_res():
    '''#This is to get pages numbers dynamically
    url_init = 'https://www.yellowpages.ca/search/si/1/Indian+Restaurant/Mississauga+ON'
    html = requests.get(url_init).content
    soup = BeautifulSoup(html,'html.parser')
    pages = soup.select_one('.pageCount > span:nth-child(2)').get_text()
    print(pages.rstrip())'''

    for i in range(1,2):
        print(f'getting page {i}')
        url = f'https://www.yellowpages.ca/search/si/{i}/Indian+Restaurant/Mississauga+ON'
        html = requests.get(url).content
        soup = BeautifulSoup(html,'html.parser')
        #cards = soup.select('div.listing > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')
        cards = soup.select('.mlr__item__cta')
        for card in cards:
            try:
                nme = card.get('title')
                if 'Get the' in nme:
                    continue
                if 'Search' in nme:
                    continue
                if 'Get direction' in nme:
                    continue
                nme = nme.replace(' - Business Website','')
            except:
                continue
            try:
                link = card.get('href')
                if 'javascript' in link:
                    link = ''
                if link is not None:
                    if 'redirect' in link:
                        link = link.split('=')
                        link = link[1]
                        link = urllib.parse.unquote(link)
                    
            except:
                link = 'no web'
            
            all_data.append([nme,link])
            
            '''if link is not None:
                if 'redirect' in link:
                    link = link.split('=')
                    link = link[1]
                    dlink = urllib.parse.unquote(link)
                    all_data.append(dlink)'''

    '''with open(r'links.txt', 'w') as fp:
        for item in all_data:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')'''
    return all_data
        
print(get_res())