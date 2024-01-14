# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import re

import bs4
import requests

url = r'https://en.wikipedia.org/wiki/Russia'

href = requests.get(url).text
soup = bs4.BeautifulSoup(href, 'html.parser')

common_data = soup.find_all('table',
                            class_='infobox ib-country vcard')[0]
tablelabels = common_data.find_all('th', class_='infobox-label')
tabledata = common_data.find_all('td', class_='infobox-data')

for label, data in zip(tablelabels, tabledata):
    head = label.text.strip()

    head = re.sub(r'\[[(0-9)]\]*', '', head)
    print(head, end=': \n')

    tset = data.find_all('li')
    if tset:
        for t in tset:
            n = ' ' * len(str(head))
            print(n, f'{t.text.strip()}')
    print(tset)

