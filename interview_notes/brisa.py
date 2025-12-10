# **Example:**
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.


input_string = "abcabcbb"

sub_strings = {}

prev_char = None
sub = []
# Get the the unique letters
for char in input_string:
    if char not in sub:
        sub.append(char)
    else:
        sub_strings.update({"".join(sub): len(sub)})
        sub = []
        sub.append(char)

# print(sub_strings)

largest = list(sub_strings.values())[0]
largest_key = list(sub_strings.keys())[0]
for key, value in sub_strings.items():
    if largest < value:
        largest_key = key

print(largest_key)

print(sub_strings[largest_key])

list_1 = [(1, "one"), (2, "two")]
dict_1 = {key: value for key, value in list_1}
print(dict_1)


def addition(func):
    def wrapper():
        func() + 1

    return wrapper


@addition
def sample():
    return 2


print(sample())

input1 = {1: "one", 2: "two", 3: {10: "ten", 9: "nine"}, 4: [5, 6, 7], 0: 0}

key_count = 0
value_count = 0
for key, value in input1.items():
    key_count = key_count + 1
    if isinstance(value, dict):
        value_count = value_count + 1
        for key2, value2 in value.items():
            key_count = key_count + 1
            value_count = value_count + 1
    elif isinstance(value, list):
        value_count = value_count + 1
    else:
        value_count = value_count + 1

print(key_count)
print(value_count)


# given a string s, write a function alternate_slicing(s, k) that returns a new string containing every k-th character from s, starting from the first character.


# For example, for k=3, it should return every third character.


def alternate_slicing(s, k):
    return s[::k]


s = "abcdefghijklmnopqrstuvwxyz"
result = alternate_slicing(s, 3)
print(result)  # Output: "adgjmpsvy"

string = "hello12  how 22"

import re

print("".join(re.findall(r"\d+", string)))

list_1 = [1, 1, 2, 2, 3, 4, 5]

# print(list(set(list_1)))

output_list = []

for item in list_1:
    if item not in output_list:
        output_list.append(item)

print(output_list)


























































































