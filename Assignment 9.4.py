filename = input("Enter file:")
fh = open(filename, 'r')
counts = dict()
for line in fh:
    if line.startswith("From "):
        line = line.rstrip()
        x = line.split(" ")
        y = x[1]
        counts[y] = counts.get(y, 0) + 1
c1 = None
c2 = None
for n, m in counts.items():
    if c1 is None or c2 < m:
        c1 = n
        c2 = m
print(c1, c2)
