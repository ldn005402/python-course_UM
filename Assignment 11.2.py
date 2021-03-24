import re
hand = open('readnum.txt')
x = 0
for line in hand:
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    if len(num) == 0:
        continue
    for pieces in num:
        x = x + int(pieces)
print("sum: ", x)
