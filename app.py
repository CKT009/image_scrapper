import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os

save_dir = "images/"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

query = "Anakin"
response = requests.get(f"https://www.google.com/search?q={query}&sca_esv=579611265&tbm=isch&sxsrf=AM9HkKktwpR6TorKx2make1fqkfxwv_AGg:1699189708877&source=lnms&sa=X&ved=2ahUKEwimm4P49qyCAxXZa2wGHeV0A9MQ_AUoBHoECAIQBg&biw=1536&bih=731&dpr=1.25")

response

soup = BeautifulSoup(response.content, 'html.parser')

images_tags = soup.find_all("img")

del images_tags[0]

for i in images_tags:
    images_url = i['src']
    image_data = requests.get(images_url).content
    with open(os.path.join(save_dir, f"{query}_{images_tags.index(i)}.jpg"), "wb") as f:
        f.write(image_data)