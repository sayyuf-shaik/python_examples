# """
# input an Excel with
# row1 1 2 3 4 5
# row2 6 7 8 9 10
# output1 1 2 3 4 5 6 7 8 9 10
# output2 1 6 2 7 3 8 4 9 5 10
# """
#
# import pandas as pd
#
# data = pd.read_excel("sample.xlsx")
# print(data)
#
def first_non_repeating_char(input_string):
  """
  Finds the first non-repeating character in a string of lowercase letters.

  Args:
      input_string: A string of lowercase letters.

  Returns:
      The first non-repeating character, or None if there are no non-repeating characters.
  """

  # Create a dictionary to store character counts
  char_counts = {}
  for char in input_string:
    char_counts[char] = char_counts.get(char, 0) + 1

  # Find the first character with a count of 1
  for char, count in char_counts.items():
    if count == 1:
      return char

  # No non-repeating characters found
  return None

# Example usage
input_string1 = "abcabcxabc"
input_string2 = "t"
input_string3 = "yuyuy"

result1 = first_non_repeating_char(input_string1)
result2 = first_non_repeating_char(input_string2)
result3 = first_non_repeating_char(input_string3)

print(f"First non-repeating character in '{input_string1}': {result1}")
print(f"First non-repeating character in '{input_string2}': {result2}")
print(f"First non-repeating character in '{input_string3}': {result3}")
