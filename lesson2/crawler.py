import requests
from bs4 import BeautifulSoup
import lxml
from download import downloader

url = "https://www.dcard.tw"
res = requests.get(url + "/f/pet")
soup = BeautifulSoup(res.text, "lxml")
for a in soup.find_all("a", class_="PostEntry_root_V6g0rd"):
    res = requests.get(url + a["href"])
    soup = BeautifulSoup(res.text, "lxml")
    tags = soup.find_all("a", class_="TopicList_topic_1XGOjs")
    if "貓" in [tag.text for tag in tags]:
        article = soup.find("article", class_="Post_root_23_VRn")
        for img in article.find_all("img"):
            downloader(img["src"])

