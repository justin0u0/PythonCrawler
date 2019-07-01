import requests
import lxml
import random
import string
from bs4 import BeautifulSoup

url = "https://www.dcard.tw"
src_url = url + "/f/pet"
res = requests.get(src_url)
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

links = []
for div in soup.find_all("div", class_="PostList_entry_1rq5Lf"):
    if div.a.text.find("貓") != -1:
        links.append(url + div.a["href"])

def downloader(src, dst):
    with requests.get(src, stream=True) as res:
        res.raise_for_status()
        with open(dst, "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

def random_string(size=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

for link in links:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "lxml")
    div = soup.find("div", class_="PostPage_innerContainer_3RSkmO")
    article = div.article
    comment = div.find("div", class_="CommentList_container_3vk7FO")
    for img in article.find_all("img"):
        downloader(img["src"], "./article/" + random_string() + ".jpg")
    for img in comment.find_all("img"):
        downloader(img["src"], "./comment/" + random_string() + ".jpg")


