url = 'http://py4e-data.dr-chuck.net/comments_1144956.json'
data = urllib.request.urlopen(url).read().decode()
js = json.loads(data)
print(js)
sum = 0

for item in js["comments"]:
    number = int(item["count"])
    sum = sum + number
print(sum)
