from bs4 import BeautifulSoup
import requests




# function that extracts all emails from a page you provided and stores them in a list
def emailExtractor(urlString):
    #print(f'trying {urlString}')
    emailList = []
    try:
        getH = requests.get(urlString)
        h = getH.content
    except:
        h = ''
    
    soup = BeautifulSoup(h, 'html.parser')

    mailtos = soup.find_all('a')

    href_lst = []
    for i in mailtos:
        
        try:
            href_lst.append(i['href'])
        except:
            continue
        
    mail = 'no mail'
    phone = 'no phone'
    for href in href_lst:
        if 'mailto:' in href :
            mail = href
        if 'tel:' in href:
            phone = href
    return [mail,phone]

def get_mail(url):
    url1 = url + 'contact'
    url2 = url + 'contact-us'
    lst = emailExtractor(url1)
    if lst[0] == 'no mail' and lst[1] == 'no phone':
        return emailExtractor(url2)
    else:
        return lst
        

