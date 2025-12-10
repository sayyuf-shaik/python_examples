"""
Write a function that takes in a string of lowercase letters and returns the first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string does not contain any non-repeating characters your function should return None

Example 1:

input_string = "abcabcxabc"

Example 2:

input_string = "t"

Example 3:

input_string = "yuyuy"
"""


def get_non_repeating_character(input_string):
    # check for lowercase letters
    frequent = dict()
    if input_string.islower():
        for char in set(input_string):
            frequent[char] = input_string.count(char)
    # print(frequent)
    frequent_list = []
    max_occurence = max(frequent.values())
    for key, value in frequent.items():
        if value >= max_occurence:
            # print(key, value)
            frequent_list.append(key)

    return frequent_list

print(get_non_repeating_character("abcabcxabc"))
print(get_non_repeating_character("t"))
print(get_non_repeating_character("yuyuy"))


