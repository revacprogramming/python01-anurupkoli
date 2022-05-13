def computepay(h, r):
    if h <= 40 :
        grosspay = h*r
    else :
        a = h-40
        grosspay = a*1.5*r+40*r
    return grosspay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate: "))
p = computepay(hrs, rate)
print("Pay", p)