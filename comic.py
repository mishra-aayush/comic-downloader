# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:26:15 2020

Script to download latest XKCD comics

@author: AAYUSH MISHRA
"""

import os
import requests
import bs4

x = int(input('To download the latest xkcd comics, enter a valid number: '))
print()

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok = True)
counter = 0

while counter < x and not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    
    if comicElem == []:
        print('Comic image not found...')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading page %s...' % (comicUrl))
        print()
        res = requests.get(comicUrl)
        res.raise_for_status()
        
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    counter += 1

print()
print('Downloaded')
print('Check xkcd folder')