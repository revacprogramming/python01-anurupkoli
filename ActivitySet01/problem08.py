# filename = "dataset/mbox-short.txt"
file_name = input("Enter the file name: ")
l = []
with open(file_name) as f:
    for line in f:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        # print(line)
        posi = line.find(":")
        string = line[posi+2:]
        # print(string)
        number = float(string)
        # print(number)
        l.append(number)
total = 0
# print(l)
no = len(l)
# print(no)
for i in l:
    total += i
avg = total/no
print("Average spam confidence:", avg)
