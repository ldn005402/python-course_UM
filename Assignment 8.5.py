fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        line = line.rstrip()
        pieces = line.split(' ')
        address = pieces[1]
        count = count + 1
        print(address)
print("There were", count, "lines in the file with From as the first word")
