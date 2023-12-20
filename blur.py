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
scraper.get_url("https://blur.io/collection/thecaptainz")
scraper.scrape_blur()