# Conditional Execution

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = float(input("Enter Rate"))

if hrs>40:
 a = hrs - 40
 
 b = a*1.5*rate
 print(b+40*rate)
    
else :
    print(rate*hrs)
