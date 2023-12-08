def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False

print("Is there alliteration?")
print(is_alliteration("this", "that"))
print(is_alliteration("tip", "tap"))
print(is_alliteration("cat", "bat"))

def count_vowels(word):
    count = 0
    vowels = 0
    for letter in word:
        if letter in "aeiou":
            vowels = vowels + 1
    return count + vowels
            
print("How many vowels are in the word?")
print(count_vowels("aeiou"))
print(count_vowels("money"))
print(count_vowels("yaasify"))

def count_numbers(word):
    count = 0
    numbers = 0
    for letter in word:
        if letter in "1234567890":
            numbers = numbers + 1
    return count + numbers

print("How many numbers are there?")
print(count_numbers("Verison67"))
print(count_numbers("3, 2, 1! Go!"))
print(count_numbers("Everyday"))

def count_target_letters(word):
    count = 0
    special = 0
    for character in word:
        if character in "a":
            special = special + 1
    return count + special

print("How many a's are in the word?")
print(count_target_letters("about"))
print(count_target_letters("again"))
print(count_target_letters("all around the wall"))

def in_alphabetical_order(word):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for letter in word:
        if letter in "abcdefghijklmnopqrstuvwxyz" and letter != alpha:
            return True
    return False

print("Is it in alphabetical order?")
print(in_alphabetical_order("bcdefg"))
print(in_alphabetical_order("untidy"))
        


