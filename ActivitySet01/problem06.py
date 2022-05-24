largest = 0
smallest = 0
list = []
while True :
    number = input("Enter the number: ")
    if number == "done" :
        break
    try :
        num = int(number)
    except :
        print("Invalid input")
    
    list.append(num)
        
largest = max(list)
smallest = min(list)
print("Maximum is", largest)
print("Minimum is", smallest)