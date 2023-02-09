from bs4 import BeautifulSoup
import re
import requests


def run(url) :
    emails = 'none'
    contact = ''
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        res = requests.get(url, headers=headers).text
    except:
        return emails
    nw_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", res, re.I))
    ml = list(nw_emails)
    if ml:
          emails = ml[0]
          emails = emails.replace('mailto:','')
          return emails
    nw_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.ca", res, re.I))
    ml = list(nw_emails)
    if ml:
          emails = ml[0]
          emails = emails.replace('mailto:','')
          return emails
    soup = BeautifulSoup(res, 'html.parser')
    for link in soup.find_all('a'):
        try:
            ref = link.get('href')
        except:
             ref = 'zzz'
        
        try:
            if 'mailto' in ref:
                    if ref.endswith('.com') or ref.endswith('.ca'):
                        return ref.replace('mailto:','')
        except:
                pass
        try:
            if 'contact' in ref:
                    contact = ref
        except:
                pass
    if contact.startswith('http'):
          contact = contact
    else:
          if 'https://' in url:
            new_url = url.replace('https://','')
          else:
            new_url = url.replace('http://','')
          contact = new_url + contact
          contact = contact.replace('//', '/')
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        res = requests.get(url, headers=headers).text
    except:
        return emails
    #soup = BeautifulSoup(res, 'html.parser')
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", res, re.I))
    eml = list(new_emails)
    if eml:
          emails = eml[0]
          emails = emails.replace('mailto:','')
          return emails
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.ca", res, re.I))
    eml = list(new_emails)
    if eml:
          emails = eml[0]
          emails = emails.replace('mailto:','')
          return emails
    # ---------------------
    return emails

def get_socials(link):
    return run(link)

#print(get_socials(' https://bombayonthelake.ca/'))

