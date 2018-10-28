#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests

start_link = "https://myactivity.google.com/myactivity"
full_pg = requests.get(start_link)

soupified_pg = bs(full_pg.text, 'lxml')

print(soupified_pg)