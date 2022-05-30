with open("dataset/mbox-short.txt") as f:

    count = 0
    for line in f:
        line = line.rstrip()
        # print(line)
        if not line.startswith("From "):
            continue
        words = line.split()
        print(words[1])
        count += 1

print(f"There were {count} lines in the file with From as the first word")
