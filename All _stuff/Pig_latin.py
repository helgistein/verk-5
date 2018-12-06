english = input("Enter a Word: ")
length = len(english)
vowel = ["a","e","i","o","u","y"]
consonant =['b, c, d, f, g, h, j, k, l, m ,n ,p, q, r, s, t, v, w, x, z']
pyg = "yay"
new_word = english

first = english[0]

ifvowel = english + pyg

if first in vowel:
    print(ifvowel)
else:
    for i in new_word:
        if new_word[0] not in vowel:
            new_word = new_word[1::] + new_word[0]
        else:
            break

    new_word += "ay"
print(new_word)
word = input("Enter a word: ")

