import csv 

def count_vowels(word):
    count = 0
    vowels = 0
    for letter in word:
        if letter in "aeiou":
            vowels = vowels + 1
    return count + vowels

f = open("09WorkingWithFiles/data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
def most_vowels(wordlist):
    count = 0
    curr_count = 0
    for word in wordlist:
        for letter in word:
            if letter in "aeiou":
                count = count + 1
                curr_count = count_vowels(word)
                if count_vowels(word) > curr_count:
                    curr_count = count_vowels(word)
            #return word, count_vowels(word)
        # decide whether the current word has more vowels than anything we've seen before
        # if so, it becomes the new winner!
print("The word with the most vowels is :", most_vowels(words))

f.close()


import csv

f = open("09WorkingWithFiles/data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
length_of_words = 0
amount_of_words = 0
for row in words:
    amount_of_words + 1
    length = int(len(words))
    length



