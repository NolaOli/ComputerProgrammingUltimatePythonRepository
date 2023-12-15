import csv 

def count_vowels(word):
    vowels = 0
    for letter in word:
        if letter in "aeiou":
            vowels = vowels + 1
    return vowels

f = open("09WorkingWithFiles/data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")

def most_vowels(wordlist):
    mostVowels = 0
    wordWithMostVowels = ""
    for word in wordlist:
        curr_count = count_vowels(word)
        if curr_count > mostVowels:
            mostVowels = curr_count
            wordWithMostVowels = (word)
    #return wordWithMostVowels, mostVowels
                
#print("The word with the most vowels is :", most_vowels(words))

f.close()


import csv

f = open("09WorkingWithFiles/data/4000-most-common-english-words.csv", "r")
wordlist = f.read().split("\n")
total_length = 0
word_amount = 0

for word in wordlist:
    if len(words) > 0:
        total_length = len(word) + total_length
        word_amount = word_amount + 1
avg_length = total_length / word_amount

print("The average wordlength of the list is:", avg_length, "letters.")

f.close()


        



