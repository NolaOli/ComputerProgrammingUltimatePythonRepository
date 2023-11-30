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