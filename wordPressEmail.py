from bs4 import BeautifulSoup
import requests
import pandas as pd

urlString = 'http://hakkakhazana.ca/contact/'


# function that extracts all emails from a page you provided and stores them in a list
def emailExtractor(urlString):
   
    emailList = []
    getH = requests.get(urlString)
    h = getH.content
    soup = BeautifulSoup(h, 'html.parser')

    mailtos = soup.find_all('a')

    href_lst = []
    for i in mailtos:
        href_lst.append(i['href'])

    for href in href_lst:
        if 'tel:' in href or 'mailto:' in href :
            emailList.append(href)
    print(emailList)

emailExtractor(urlString)
