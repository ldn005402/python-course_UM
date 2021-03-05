hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
except:
    print("not a number")

try:
    r = float(rate)
except:
    print("not a number")
    
if h > 40:
    s1 = (h-40) * (r*1.5)
    s2 = 40 * r
    st = s1 + s2
else:
    st = h * r

print(st)
