with open("Longest.txt", "r") as f:
    longest_word = ""
    for line in f:
        if len(line.strip()) >= len(longest_word):
            longest_word = line.strip()

    print("Longest word is",  "'"+longest_word+"'" , "of length", len(longest_word), end=" ")
    