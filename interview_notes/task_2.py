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
    if input_string.islower():
        for char in input_string:
            if input_string.count(char) == 1:
                return char
        return None


print(get_non_repeating_character("abcabcxabc"))
print(get_non_repeating_character("t"))
print(get_non_repeating_character("yuyuy"))


