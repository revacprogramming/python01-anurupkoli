
with open("dataset/romeo.txt") as f:
    fh = f.read()
    fh = fh.split()
    list = []
    for word in fh:
        if word not in list:
            list.append(word)
list.sort()
print(list)


