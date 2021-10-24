from urllib.request import urlopen
from bs4 import BeautifulSoup
a = urlopen("http://python.org")
soup = BeautifulSoup(a.read(), "html.parser")
print(soup.h1)