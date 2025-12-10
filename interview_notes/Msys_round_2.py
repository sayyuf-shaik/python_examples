# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

# Write code to extract integers from string and return a sorted integer list.

# i/p :  ms1875yste21chno1o19gies101

# o/p : 1 19 21 101 1875

string = "ms1875yste21chno1o19gies101"

import re

matches = re.findall("\d+", string)

integer_list = list(map(lambda x: int(x), matches))

for i in range(len(integer_list)):
    for j in range(i):
        if integer_list[i] < integer_list[j]:
            integer_list[i], integer_list[j] = integer_list[j], integer_list[i]

print(integer_list)

    # Reverse a string without changing the index positions of the special characters .

    # I/p : Ab%c&de!$

    # o/p : ed%c&bA!$

string = "Ab%c&de!$"

stripped_string = ""

for char in string:
    if char.isalpha():
        stripped_string = stripped_string + char
        string = string.replace(char, "0")

stripped_string = stripped_string[::-1]

for char in stripped_string:
    string = string.replace("0", char, 1)

print(string)

# nested list :
# [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]

# flat list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


nested_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = []

# for element in nested_list:
#     if isinstance(element, list):
#         for i in element:
#             if isinstance(i, list):
#                 flat_list.extend(i)
#             else:
#                 flat_list.append(i)
#     else:
#         flat_list.append(element)
#
# print(flat_list)

# Optimised solution:
# this is a very tricky question
# Optimizing this would involve using recursion and generator


def flatten(data):
    for ele in data:
        if isinstance(ele, list):
            yield from flatten(ele)
            # yield from will divide the task among the generators
        else:
            yield ele


print(list(flatten(nested_list)))

























