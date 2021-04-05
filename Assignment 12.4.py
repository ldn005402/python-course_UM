import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = 'http://py4e-data.dr-chuck.net/comments_1144953.html'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')


tags = soup('span')
total = 0
for tag in tags:
    x = str(tag)
    y = re.findall("[0-9]+", x)
    for num in y:
        num = int(num)
        total = total + num
print(total)
