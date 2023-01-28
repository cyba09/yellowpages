from bs4 import BeautifulSoup
import requests
import pandas as pd
import yellow
import facebook_scrape
import wordPressEmail

What = 'Indian Restaurant'
Where = 'Mississauga ON'

def get_page_count(link):
    res = requests.get(link).content
    soup = BeautifulSoup(res,'html.parser')
    num = soup.select_one('.pageCount > span:nth-child(2)').get_text().rstrip()
    return int(num) + 1

main_data = []
cnt = 1
if __name__ == "__main__":
    query_str = 'https://www.yellowpages.ca/search/si'
    What = What.replace(' ','+')
    Where = Where.replace(' ','+')
    link = f'{What}/{Where}'
    pge = get_page_count(f'{query_str}/1/{link}')
    lst = yellow.parse_data(pge,link)
    for rest in lst:
        print(f'getting link {cnt} of {len(lst)}')
        cnt += 1
        web = rest['Website']
        if web == '':
            ls = ['','']
        else:
            if 'facebook' in web:
                ls = facebook_scrape.get_facebook(web)
            else:
                ls = wordPressEmail.get_mail(web)
        main_data.append({'Name' : rest['Name'],
                    'City' : rest['City'],
                    'Telephone' : rest['Phone'],
                    'Website' : rest['Website'],
                    'Email' : ls[0],
                    'Phone' : ls[1]})
    df = pd.DataFrame(main_data)
    df.to_excel('yellowpages.xlsx', index=False)
    
