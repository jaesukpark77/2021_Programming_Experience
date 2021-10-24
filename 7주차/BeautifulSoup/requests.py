import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://newsstand.naver.com/?list=&pcode=011'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
print('Beautifulsoup의 html parser을 이용해 나온 형태는: ', soup)
print('url을 get으로 받아온 형태는: ', req)
print('#' * 20)
html = req.text
print('get으로 받아온 후의 문자열만 추출한 것은: ', html)
print('#' * 20)
soup = BeautifulSoup(html, 'html.parser')
print('Beautifulsoup의 html parser을 이용해 나온 형태는: ', soup)
