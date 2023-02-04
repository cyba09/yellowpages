from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
import re



def run(playwright: Playwright, url) -> None:
    emails = 'none'
    contact = ''
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    html1 = page.inner_html('body')
    soup = BeautifulSoup(html1, 'html.parser')
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
    page.goto(url)
    html = page.inner_html('body')
    soup = BeautifulSoup(html1, 'html.parser')
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", html, re.I))
    eml = list(new_emails)
    if eml:
          emails = eml[0]
          emails = emails.replace('mailto:','')
    
    # ---------------------
    context.close()
    browser.close()
    return emails

def get_socials(link):
        with sync_playwright() as playwright:
                return run(playwright,link)

print(get_socials('http://www.indiancuisinebythelake.com/'))

