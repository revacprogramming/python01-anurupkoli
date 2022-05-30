
with open("dataset/mbox-short.txt") as f :
    dict ={}
    list = []
    for lines in f:
        lines = lines.rstrip()
        # print(lines)
        if lines.startswith("From"):
            line = lines.split()
            # print(line)
            dict[line[1]] = dict.get(line[1], 0) + 1

# print(dict)
value = 0
word = None
for w,v in dict.items():
    if v > value:
        value = v
        word = w
print(word,value)

