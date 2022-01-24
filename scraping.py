import requests
from bs4 import BeautifulSoup
url = "http://localhost:63342/popup/menu.html?_ijt=ffpgf46rs0krf553l1n6l6ujn2"

r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")

elems = soup.find_all("a",class_="refarence internal")
for e in elems:
    print(e.getText())

