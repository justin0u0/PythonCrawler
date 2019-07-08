import random
import string
import requests

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

