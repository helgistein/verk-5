s = (input("Enter string: "))
punctuation = (',', '.', '?')
count = {"UPPER": 0, "LOWER": 0, "DIGIT": 0, "punctuation": 0}

for i in s:
    if i.isupper():
        count["UPPER"] += 1
    elif i.islower():
        count["LOWER"] += 1
    elif i.isdigit():
        count["DIGIT"] += 1
    elif i in punctuation:
        count["punctuation"] += 1
    else:
        pass

print("Enter a sentence:", s )
print("{0:>15s} {1:5d}".format("Upper case", count["UPPER"]))
print("{0:>15s} {1:5d}".format("Lower case", count["LOWER"]))
print("{0:>15s} {1:5d}".format("Digits", count["DIGIT"]))
print("{0:>15s} {1:5d}".format("Punctuation", count["punctuation"]))