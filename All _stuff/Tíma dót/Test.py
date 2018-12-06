with open("text.txt", "r") as f:
    for line in f:

        stripped = line.strip().replace(" ", "")
        print(stripped, end="")
