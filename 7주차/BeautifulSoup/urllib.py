from urllib.request import urlopen       #url을 여는 모듈
from bs4 import BeautifulSoup            #Beautiful Soup
a = urlopen("http://python.org")
soup = BeautifulSoup(a.read(), "html.parser") #a를 호출해 html을 parser
print(soup.h1)                           #soup에서 <h1> 부분만을 출력함
