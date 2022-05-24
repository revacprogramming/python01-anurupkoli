
text = "X-DSPAM-Confidence:    0.8475"
posi = text.find(":")
strip = text[posi+5:]
# print(posi)
# print(strip)
number = float(strip)
print(number)