fname = input("Enter file name: ")
fh = open(fname, 'r')
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        x = line.find(":")
        y = float(line[x+2:])
        count = count + 1
        total = total + y
avg = total / count
print("Average spam confidence:", avg)
