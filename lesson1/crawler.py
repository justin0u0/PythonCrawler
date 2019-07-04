import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://iogames.fun'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
# print (soup.prettify())

links = soup.find_all("a", class_="tiles-item")
for link in links:
    print(url + link["href"])

""" You can also do this
for link in soup.find_all("a", class_="tiles-item"):
    print(url + link["href"])
"""

