import requests
from bs4 import BeautifulSoup
r = requests.get("https://cyclobold.com/")
data = BeautifulSoup(r.content, "html.parser")
data = data.prettify()
print(data)