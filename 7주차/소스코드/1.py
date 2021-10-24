import urllib.request
a = urllib.request.urlopen("http://computing.or.kr")
print(a.read())