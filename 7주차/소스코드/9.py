from urllib.request import urlopen           #url을 여는 모듈
from bs4 import BeautifulSoup                #Beautiful Soup
a = urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
soup = BeautifulSoup(a.read(), "html.parser")
movie = soup.find_all('div', 'tit3')
print(movie)
i = 1
for a in movie:
    print("%d위 : %s" %(i, a.find('a').text))
    i += 1

