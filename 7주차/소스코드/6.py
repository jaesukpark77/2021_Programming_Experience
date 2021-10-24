from urllib.request import urlopen
from bs4 import BeautifulSoup

with open("c:/temp/example.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
    a = soup.find_all('div', 'ABC_class`')
    print(a)
