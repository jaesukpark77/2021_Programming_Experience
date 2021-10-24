from urllib.request import urlopen
from bs4 import BeautifulSoup                #Beautiful Soup
a = urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
soup = BeautifulSoup(a.read(), "html.parser")
print(soup.title)

