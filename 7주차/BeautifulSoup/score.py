import requests
from bs4 import BeautifulSoup

data = requests.get('https://music.bugs.co.kr/chart')
soup = BeautifulSoup(data.text, 'html.parser')
## print(soup)
rank_lists = soup.select('.list > tbody > tr')
print(rank_lists)

for rank_list in rank_lists:
    ranking = rank_list.select_one('td > div.ranking > strong').text
    m_title = rank_list.select_one('th > .title > a').text
    m_artist = rank_list.select_one('td.left > .artist > a').text
    print(ranking, m_title, m_artist)
