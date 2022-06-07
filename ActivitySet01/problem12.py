with open("dataset/mbox-short.txt") as fh :
    list = []
    dict = {}
    for lines in fh:
        lines = lines.rstrip()
        if not lines.startswith("From "):
            continue
        lines = lines.split()
        list.append(lines[5])    
        
        
for hrs in list:
    hrs = hrs.split(":")
    dict[hrs[0]] = dict.get(hrs[0], 0)+1

# print(dict)
list2 = []
for k,v in dict.items():
    list2.append((k,v))
list2 = sorted(list2)
for k,v in list2:
    print(k,v)