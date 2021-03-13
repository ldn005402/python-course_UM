fname = input("Enter file name: ")
fh = open(fname)
wl = list()
for line in fh:
    line = line.rstrip()
    x = line.split(' ')
    for words in x:
        if words not in wl:
            wl.append(words)
wl.sort()
print(wl)
