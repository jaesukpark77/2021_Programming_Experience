from bs4 import BeautifulSoup

with open("c:/temp/example.html", encoding="UTF-8") as f:
    soup = BeautifulSoup(f, "html.parser")

    a = soup.find("div")
    print(a)
