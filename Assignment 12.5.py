import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Franco.html'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
position = int(input("Enter a position:"))-1
repeat = int(input("How many times:"))
sequence = []
tags = soup('a')
for i in range(repeat):
    link = tags[position].get('href', None)
    sequence.append(tags[position].string)
    html = urllib.request.urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(sequence[-1])
