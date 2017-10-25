from bs4 import BeautifulSoup
import requests


r = requests.get("https://en.wikipedia.org/wiki/Tendulkar")

data = r.text

soup = BeautifulSoup(data)

soup1 = soup.prettify()
for link in soup.find_all(attrs={'class': 'infobox vcard'}):
    print(link.text)

