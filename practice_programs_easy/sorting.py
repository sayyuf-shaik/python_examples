##
# Selection sort
# {64, 25, 12, 22, 11}
# 11 lowest value

list_ = [64, 25, 12, 11]


def selection(list_):
    for i in range(len(list_)):
        smallest = i
        for j in range(i + 1, len(list_)):
            if list_[smallest] > list_[j]:
                smallest = j

        list_[i], list_[smallest] = list_[smallest], list_[i]
    return list_


# selection(list_)

## BUBBLE SORT ALGO
# sort array by moving the larget element everytime to rightmost place
# {6, 3, 0, 5}
# pass 1 --> { 6 3 0 5}
# 6 > 3 swap --> {3 6 0 5}
# 6 > 0 swap --> {3 0 6 5}
# 6 > 5 swap --> {3 0 5 6}
# pass 2 --> {3 0 5 6}
# 3 > 0 --> {0 3 5 6}
# 3 > 5 keep
# pass 3 {0 3 5 6}
# 5 > 6 keep
# Array sorted {0 3 5 6}

def bubblesort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# print(bubblesort([6, 3, 0, 5]))
## Insertion SOrt
# {12, 11, 13, 5, 6}
# Pass1
# 11 < 12 yes keep {11 12 13 5 6}
#     --> check if any before values no
# 12 < 13 yes keep {11 12 13 5 6}
# 13 < 5 no swap [11 12 5 13 6]
#     --> 5 > 12 swap {11 5 12 13 6}
#     --> 5 > 11 swap {5 11 12 13 6}
# 13 < 6 no swap {5 11 12 6 13]
#  --->  6 > 12 no swap {5 11 6 12 13}
# -----> 6 > 11 no swap {5 6 11 12 13}
# ----> 6 > 5 yes keep { 5 6 11 12 13}


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        # Consider the second element in the list as key i .e first element in the loop iterating
        # Since we're iterating from 1 of actual list rather than 0
        key = numbers[i]
        # This index j will be used to traverse back from the key i.e. for checking any values
        # that are less than the current key's position before elements
        j = i - 1
        # Compare the key with every element that is before the key till start of the list
        # if the values are less then you can move the elements one position up
        while j >= 0 and key < numbers[j]:
            # If key is less than before number then move the key value index that is j +1 to j
            numbers[j + 1] = numbers[j]
            j -= 1 # -1
        numbers[j + 1] = key # 11
    return numbers

# print(insertion_sort([12, 11, 13, 5, 6]))

## Merge Sort
#



