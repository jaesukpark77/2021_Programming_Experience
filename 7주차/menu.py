from bs4 import BeautifulSoup
a = open("c:/temp/menu.html", 'r', encoding="UTF-8")
soup = BeautifulSoup(a.read(), 'html.parser')
#result = soup.find_all('p', class_='each-menu')
result = soup.find_all('p', 'each-menu')
for data in result :
    print(data.text)

