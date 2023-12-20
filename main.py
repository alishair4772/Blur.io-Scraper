from functions import MemeLand
import pandas as pd
import os

scraper = MemeLand()
urls = scraper.generate_urls()
scraper.launch_chrome()

txt = open('login.txt')
lines = txt.readlines()
wallet_phrase = lines[0].split(" ")
password = lines[1]

scraper.login_metamask(phrase=wallet_phrase,password=password)

for url in urls:
    data = {'Captainz ID':[],'questing':[],'price':[],'Total Mapz':[],'Unrevealed': [], 'Special': [], 'Extraordinary': [], 'Magical': [], 'Epic': [], 'Mythical': []}
    scraper.get_url(url)
    scraper.scrape(data=data)
    path = os.listdir()

    if 'data.csv' in path:
        df = pd.DataFrame(data,columns=list(data.keys()))
        df.to_csv(f'data.csv', mode='a',index=False,header=False)
    else:
        df = pd.DataFrame(data, columns=list(data.keys()))
        df.to_csv(f'data.csv', mode='a', index=False, header=True)
