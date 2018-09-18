english = input("Enter a word: ")
length = len(english)
vowel = ["a","e","i","o","u","y"]

pyg = "yay"


while english != ".":
    new_word = english
    first = new_word[0]
    ifvowel = new_word + pyg
    if first in vowel:
        new_word = english + pyg
    else:
        for i in new_word:
            if new_word[0] not in vowel:
                new_word = new_word[1::] + new_word[0]
            else:
                break

        new_word += "ay"
    print(new_word)
    english = input("Enter a word: ")
    


