fname = input("Enter file name: ")
fh = open(fname,'r')
for line in fh:
    lin = line.rstrip()
    print(lin.upper())
