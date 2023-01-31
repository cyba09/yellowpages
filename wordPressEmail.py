import requests
from bs4 import BeautifulSoup

extensions = ['contact', 'contact-us', 'contact.html', 'contact-us.html']

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
        
    mail = ''
    phone = ''
    for href in href_lst:
        if 'mailto:' in href :
            mail = href
            mail = mail.replace('mailto:','')
        if 'tel:' in href:
            phone = href
            phone = phone.replace('tel:','')
    return [mail,phone]

def get_mail(url):
    for ext in extensions:
            lst = emailExtractor(url + ext)
            if lst[0] != '' or lst[1] != '':
                break
    return lst

