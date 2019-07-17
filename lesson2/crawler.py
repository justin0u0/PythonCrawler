import solver
from bs4 import BeautifulSoup
import lxml
import time

res = requests.get("https://www.dcard.tw/f/pet")
soup = BeautifulSoup(res.text, "lxml")
for a in soup.find_all("a", class_="PostEntry_root_V6g0rd"):
    time.sleep(1)
    res = requests.get("https://www.dcard.tw" + a["href"])
    soup = BeautifulSoup(res.text, "lxml")
    tags = soup.find_all("a", class_="TopicList_topic_1XGOjs")
    if "貓" in [tag.text for tag in tags]:
        article = soup.find("article", class_="Post_root_23_VRn")
        for img in article.find_all("img"):
            solver.downloader(img["src"])

