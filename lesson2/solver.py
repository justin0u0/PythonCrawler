import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_ip_list():
    ua = UserAgent()
    url = "https://www.xicidaili.com/"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": ua.random
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    trs = soup.find_all("tr")
    ips = []
    for tr in trs:
        tds = tr.find_all("td")
        try:
            if tds[4].text == "高匿":
                ips.append(tds[1].text + ":" + tds[2].text)
        except:
            pass
    # print(ips)
    return ips

import random
def get(url):
    proxy_list = []
    ip_list = get_ip_list()
    for ip in ip_list:
        proxy_list.append("http://" + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {"http": proxy_ip}
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    return requests.get(url, headers=headers, proxies=proxies)

import string
def downloader(src):
    print(f"Downloading {src} ...")
    with requests.get(src, stream=True) as res:
        res.raise_for_status()
        fn = "./images/" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + ".jpg"
        with open(fn, "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print("Done.")

