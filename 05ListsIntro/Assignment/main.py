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
    
    