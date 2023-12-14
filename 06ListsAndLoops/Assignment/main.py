def count_failing_grades(inputlist):
    count = 0
    for percent in inputlist:
        if percent < 60:
            count = count +1

    return count
    
inputlist = [69, 78, 53, 42, 60, 35, 17, 59]
returnValue = count_failing_grades(inputlist)
print("In the list, how many students have failing grades?")
print(returnValue)

def count_act_scores(inputlist):
    count = 0
    for score in inputlist:
        if score >= 1 and score <= 36:
            count = count + 1

    return count

inputlist = [0, 5, 10, 34, 68, 28, 14, 59]
returnValue = count_act_scores(inputlist)
print("Valid ACT scores: ")
print(returnValue)

def number_sum(inputlist):
    total = 0
    for number in inputlist:
        total = total + number

    return total

inputlist = [5, 7, 10]
result = number_sum(inputlist)
print("Sum of list: ", result)

def average_act_score(inputlist):
    count = 0
    total = 0
    for score in inputlist:
        if score >= 1 and score <= 36:
            count = count + 1
            total = total + score

    return total / count

inputlist = [0, 20, 5, 50, 10, 80, 35, 32, 29]
result = average_act_score(inputlist)
print("Average ACT score: ")
print(result)

def all_true(list):
    boolean1 = list[0]
    boolean2 = list[1]
    boolean3 = list[2]
    for boolean in list:
        if boolean1 == "True" and boolean2 == "True" and boolean3 == "True":
            return True
    else:
        return False
    
print("Is boolean list all true?")
print(all_true(["True", "True", "True"]))
print(all_true(["True", "False", "True"]))
print(all_true(["False", "False", "False"]))
print(all_true(["True", "True", "True"]))
print(all_true(["True", "True", "False"]))
    
def any_true(item):
    variable1 = item[0]
    variable2 = item[1]
    variable3 = item[2]
    for variable in item:
        if variable1 == "True":
            return True
        elif variable2 == "True":
            return True
        elif variable3 == "True":
            return True
        else:
            return False
        
print("Are any values true?")
print(any_true(["True", "True", "True"]))
print(any_true(["False", "False", "False"]))
print(any_true(["False", "True", "False"]))
print(any_true(["False", "False", "True"]))
print(any_true(["True", "False", "False"]))

def has_vowel(letters):
    for letter in letters:
        if letter in ["a", "e", "i", "o", "u"]:
            return True
    return False

print("Does list have vowel?")      
print(has_vowel(["l", "f", "j", "k", "i"]))
print(has_vowel(["f", "f", "j", "g", "m"]))
print(has_vowel(["a", "f", "q", "p", "l"]))
print(has_vowel(["l", "m", "n", "q", "h"]))
print(has_vowel(["a", "b", "c", "d", "e"]))

def all_the_same(integer):
    item1 = integer[0]
    item2 = integer[1]
    item3 = integer[2]
    for item in integer:
        if item1 == item2 and item2 == item3:
            return True
    return False

print("Are all the number in the list the same?")
print(all_the_same([5, 10, 15, 20]))
print(all_the_same([5, 5, 5, 5]))
print(all_the_same([6, 6, 6, 6]))
print(all_the_same([1, 2, 4, 5]))
print(all_the_same([7, 7, 7, 7]))

def increasing(integer):
    item1 = integer[0]
    item2 = integer[1]
    item3 = integer[2]
    for item in integer:
        if item2 > item1 and item3 > item2:
            return True
    else:
        return False
    
print("Is the line increasing?")
print(increasing([1, 2, 3]))
print(increasing([4, 5, 6]))
print(increasing([5, 6, 3]))
print(increasing([1, 4, 2]))
print(increasing([10, 11, 12]))

def is_incrementing(integer):
    item1 = integer[0]
    item2 = integer[1]
    item3 = integer[2]
    for item in integer:
        if item2 == item1 + 1 and item3 == item2 + 1:
            return True
        else:
            return False
        
print("Is the line incrementing?")
print(is_incrementing([1, 2, 3]))
print(is_incrementing([1, 3, 4]))
print(is_incrementing([7, 8, 9]))
print(is_incrementing([5, 5, 5]))

def has_adjacent_repeat(integer):
    item1 = integer[0]
    item2 = integer[1]
    item3 = integer[2]
    for item in integer:
        if item1 == item2:
            return True
        elif item1 == item3:
            return True
        elif item2 == item3:
            return True
        else:
            return False
        
print("Is there an adjacent repeat in the list?")
print(has_adjacent_repeat([1, 2, 2]))
print(has_adjacent_repeat([1, 2, 3]))
print(has_adjacent_repeat([3, 6, 7]))
print(has_adjacent_repeat([6, 6, 6]))




