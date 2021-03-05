def computepay(h, r):
    if h > 40:
        return (h - 40) * (1.5 * r) + 40 * r
    else:
        return h * r

try: 
    hrs = input("Enter Hours:")
except:
    print("not a number")

try:
    rate = input("Enter Rate:")
except:
    print("not a number")


h = float(hrs)
r = float(rate)
print("Pay", computepay(h,r))
