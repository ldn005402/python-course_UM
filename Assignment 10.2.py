filename = input("Enter file:")
fh = open(filename, 'r')
counts = dict()
for line in fh:
    if line.startswith("From "):
        line = line.rstrip()
        x = line.split(" ")
        y = x[6]
        z = y.split(":")
        s = z[0]
        counts[s] = counts.get(s, 0) + 1

tup = list()
for k,v in counts.items():
    newtup = (k,v)
    tup.append(newtup)

tup.sort()

for k,v in tup:
    print(k,v)
