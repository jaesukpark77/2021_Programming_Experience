from bs4 import BeautifulSoup

with open("c:/temp/example.html", encoding="UTF-8") as f:
    soup = BeautifulSoup(f, "html.parser")

    a = soup.find_all('div', {'id':'ABC_id'})
    #a = soup.find('div', {'id':'ABC_id'}).text
    print(a)
