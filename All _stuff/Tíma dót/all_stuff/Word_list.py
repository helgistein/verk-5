import string

#build_wordlist() function goes here
def build_wordlist(infile):
    wordlist = []
    for line in infile.readlines():
        for word in line.split():
            trans = str.maketrans("","",string.punctuation)
            word = word.strip().translate(trans)
            wordlist.append(word)
    return wordlist
    

#find_unique() function goes here
def find_unique(wordlist):
    return list(set(wordlist))
    


def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()