# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#
#
# dict_1 = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
#           'nine': '9', 'ten': '10', 'eleven': '11'}
import re

# while True:
#     input_string = input("Provide key value pair:")
#     key, value = input_string.split()
#     if len(dict_1.keys()) > 10:
#         print("More than 10 values")
#         break
#     dict_1[key] = value
# print(dict_1)
# new_list = []
# for key, value in dict_1.items():
#     new_list.append((key, value))

# for i in range(len(new_list)):
#     for j in range(i - 1):
#         if new_list[i][1] > new_list[i + 1][1]:
#             new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]

# print(new_list)

# dict_1.pop("eleven")
# print(dict_1)
# import re
# string = "this is python this is python this is python"

# word_list = []
# for word in string.split():
#     if word not in word_list:
#         word_list.append((word, len(re.findall(word, string))))

# print(word_list)

# class A:
#     def __init__(self):
#         self.name = "a"
#
#     def method(self):
#         print("I m in class a")
#
#     def common(self):
#         print("This is a common method")
#
#
# class B(A):
#     def __init__(self):
#         self.name = "b"
#
#     def method(self):
#         print("I m in class b")
#
#
# obj_a = A()
# obj_a.method()
# obj_b = B()
# obj_b.common()


##
#
# input_1 = {1: "assje", 2: ["jkle", ["assfe", "abcd"], "lhhl"], 3: "erkklk"}
# output = [1, "essje", 2, ["eklj", ["essfa", "dbca"], "lhh1"], 3, "krkkle"]
#
#
#
#
#
# dict_1 = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
#           'nine': '9', 'ten': '10', 'eleven': '11'}
# values_dict = dict_1.values()

string = "this is python this is python this is python"

unique_words = {}
# without regular expression
for word in string.split():
    if word in unique_words:
        unique_words[word] += 1
    else:
        unique_words[word] = 1
print(unique_words)

# Using regular expression
words = set(string.split())

for word in words:
    count = len(re.findall(r"\b" + word, string))
    print(f"{word}: {count}")

# Find the longest substring without repeating characters.

string = "I am sayyuf and I want get laid! I am fucking virgin still"

non_duplicate_words = [] # [5, 4, 19, 2, 11]

for word in string.split():
    if len(word) == len(set(word)):
        non_duplicate_words.append((word, len(word)))

largest = non_duplicate_words[0]
second_largest = non_duplicate_words[0]

for word, length in non_duplicate_words:
    if length > largest[1]:
        second_largest = largest
        largest = (word, length)
    elif length > second_largest[1]:
        second_largest = (word, length)
print(largest)
print(second_largest)

list_1 = [5, 4, 19, 2, 11]

# large = list_1[0]
# seen = list_1[0]
# for element in list_1:
#     if element > large:

for i in range(len(list_1)):
    for j in range(len(list_1) - i - 1):
        if list_1[j] > list_1[j+1]:
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]

print(list_1)
