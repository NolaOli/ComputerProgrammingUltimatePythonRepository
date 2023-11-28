def make_abc():
    result = ["a","b","c"]
    return result

print("Demonstrate making abc:")
print(make_abc())

def equal_edges(items):
    first = items[0]
    last = items[-1]

    if first == last:
        return True
    else:
        return False
    
print("Are the edges equal?")
print("[1, 2, 3] ->", equal_edges([1, 2, 3]))
print("[2, 1, 3, 2] ->", equal_edges([2, 1, 3, 2]))

def common_edge(list1, list2):
    first1 = list1[0]
    last1 = list1[-1]
    first2 = list2[0]
    last2 = list2[-1]

    if first1 == first2 or first1 == last2:
        return True
    elif last1 == first2 or last1 == last2:
        return True
    else:
        return False
    
print("Any common edges?")
print("[1, 2, 4] & [2, 3, 4] ->", common_edge([1, 2, 4], [2, 3, 4]))
print("[1, 5, 7] & [2, 5, 8] ->", common_edge([1, 5, 7], [2, 5, 8]))

def all_the_same(item):
    first = item[0]
    second = item[1]
    third = item[2]

    if first == second and first == third:
        return True
    else:
        return False
    
print("Are all numbers the same?")
print("[2, 2, 2] ->", all_the_same([2, 2, 2]))
print("[1, 2, 2] ->", all_the_same([1, 2, 2]))

def all_unique(item):
    first = item[0]
    second = item[1]
    third = item[2]

    if first == second or first == third:
        return False
    elif second == third:
        return False
    else:
        return True
    
print("Are the numbers each unique?")
print("[1, 2, 3] ->", all_unique([1, 2, 3]))
print("[1, 2, 1] ->", all_unique([1, 2, 1]))
print("[4, 4, 3] ->", all_unique([4, 4, 3]))
print("[6, 5, 9] ->", all_unique([6, 5, 9]))

def increasing(item):
    first = item[0]
    second = item[1]
    third = item[2]

    if first < second and second < third:
        return True
    else: 
        return False
    
print("Is the list increasing?")
print("[1, 2, 3] ->", increasing([1, 2, 3]))
print("[4, 5, 6] ->", increasing([4, 5, 6]))
print("[10, 12, 4] ->", increasing([10, 12, 4]))

def all_true(item):
    argument1 = item[0]
    argument2 = item[1]
    argument3 = item[2]

    if argument1 == True and argument2 == True and argument3 == True:
        return True
    else:
        return False
    
print("Are all values true?")
print("True, True, True ->", all_true([True, True, True]))
print("True, False, True ->", all_true([True, False, True]))
print("False, False, False ->", all_true([False, False, False]))

def mostly_true(item):
    argument1 = item[0]
    argument2 = item[1]
    argument3 = item[2]

    if argument1 == True and argument2 == True and argument3 == True:
        return True
    elif argument1 == True and argument2 == True:
        return True
    elif argument2 == True and argument3 == True:
        return True
    else:
        return False
    
print("Is the list mostly true?")
print("True, True, False ->", mostly_true([True, True, False]))
print("True, False, False ->", mostly_true([True, False, False]))
print("False, True, True ->", mostly_true([False, True, True]))
print("True, True, True ->", mostly_true([True, True, True]))
print("False, False, False ->", mostly_true([False, False, False]))