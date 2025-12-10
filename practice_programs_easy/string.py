# input = a1bb2ccc3dddd4eeeee5
# output  = [(a, 1), (b, 2), (c, 3)]
import re

input_string = "a1bb2ccc3dddd4eeeee5"

# pairs = []
# count_found = False
# prev_char = input_string[0]
# for char in input_string:
#     if char != prev_char and not count_found:
#         pairs.append((prev_char, char))
#         count_found = True
#     else:
#         count_found = False
#     prev_char = char
#
# print(pairs)

letters = []

for char in input_string:
    if char.isalpha():

