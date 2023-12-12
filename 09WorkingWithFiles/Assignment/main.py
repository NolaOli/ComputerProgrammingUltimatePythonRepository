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
    vowel_count = 0
    vowel_max = 0
    for word in wordlist:
        if letter in "aeiou":
        # count the number of vowels in the current word
        cur_count = count_vowels(word)

        # decide whether the current word has more vowels than anything we've seen before
        # if so, it becomes the new winner!


    
print("The word with the most vowels is :", most_vowels(words))


f.close()


#import csv

#f = open("09WorkingWithFiles/data/4000-most-common-english-words.csv", "r")
#words = f.read().split("\n")
#length_of_words = 0
#amount_of_words = 0
#for row in words:
    #amount_of_words + 1
    #length = int(len(words))
    #length of words 



