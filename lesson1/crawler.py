import requests
from bs4 import BeautifulSoup

url = 'http://iogames.fun'
res = requests.get(url)
# print (res.text)

soup = BeautifulSoup(res.text, 'lxml')
# print (soup.prettify())

tiles = soup.find_all('div', class_='tiles')
links = []
for tile in tiles:
    for a in tile.find_all('a', class_='tiles-item'):
        links.append(a['href'])

for link in links:
    print (url + link)

