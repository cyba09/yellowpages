from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup

#first test
def run(playwright: Playwright, link1) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(link1)
    html  = page.inner_html('.xnp8db0')
    soup = BeautifulSoup(html, 'html.parser')
    try:

        email = soup.select_one('div.x1ja2u2z:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)').get_text()
        print(email)
    except:
        try:

            website = soup.select_one('').get_text()
            print(f'no email found website is {website}')
        except:
            print('no email and web address')
    # ---------------------
    context.close()
    browser.close()
    
link = 'https://www.facebook.com/TheShishMahal/'


with sync_playwright() as playwright:
    run(playwright,link)