from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
import time

#first test
def run(playwright: Playwright, link1):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.locator("#email").fill('noahmiller394@yahoo.com')
    page.locator("#pass").fill('345678iuhgvbnjk')
    page.locator("button").click()
    time.sleep(4)
    page.goto(link1)
    page.wait_for_url(link1)
    html = page.inner_html('body') #
    soup = BeautifulSoup(html, 'html.parser')
    try:

        email = soup.select_one('div.x1ja2u2z:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)').get_text().rstrip()
    except:
        email = ''
    try:
        phone = soup.select_one('div.x1nhvcw1:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)').get_text().rstrip()
    except:
        phone = ''
       
    # ---------------------
    context.close()
    browser.close()
    return [email,phone]
    

def get_facebook(link):
    with sync_playwright() as playwright:
        return run(playwright,link)

#print(get_facebook('https://www.facebook.com/TheShishMahal/'))



