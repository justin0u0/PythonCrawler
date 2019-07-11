import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    'User-Agent': 'Googlebot'
}
res = requests.get("https://shopee.tw/search?keyword=%E8%B2%93%E7%BD%90%E9%A0%AD&page=0&sortBy=relevancy", headers=headers)
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

items = soup.find_all("div", class_="shopee-search-item-result__item")
for item in items:
    link = item.find("a")["href"]
    name = item.find("div", class_="_1NoI8_ _2gr36I").text
    price = item.find("span", class_="_341bF0").text
    print("https://shopee.tw" + link)
    print(name)
    print(price + "元")
    print()

