# Nested List Comprehensions: Given a list of lists representing matrices,
# write a list comprehension to create a new list where each element is
# the sum of corresponding elements across all inner lists.
# (Example: Input: [[1, 2], [3, 4], [5, 6]]  Output: [4, 6, 11])

# [
# [1, 2],
# [3, 4],
# [5, 6],
# ]

# [1, 3 ,5]
# [2, 4, 6]

# TODO: Gave me a headache will come back later

#2. Conditional List Comprehensions with Multiple Conditions: Write a list comprehension that iterates through a list
# of strings and returns a new list containing only strings that start with a vowel and
# end with a consonant (case-insensitive).

strings = ["afjdkfdkf", "akdfjki", "egggfhfh", "ghghghgh"]

mod_strs = [string for string in strings if string[0] in "aeiou" and string[-1] not in "aeiou"]

print(mod_strs)

# 3. List Comprehensions with Dictionary Lookups: You have a list of names and a dictionary mapping names to their ages.
# Write a list comprehension that creates a new list of tuples where the first element is the
# name and the second element is the age retrieved from the dictionary (assuming all names exist in the dictionary).

names = ["sayyuf", "monica", "marivel"]

ages = {
    "sayyuf": 27,
    "monica": 26,
    "marivel": 28
}

name_age_pairs = [(name, age) for name, age in ages
                  .items()
                  ]

print(name_age_pairs)

# 4. Flattening Nested Lists: Given a list containing nested lists of arbitrary depth,
# write a list comprehension that flattens the entire structure into a single list with all elements at the same level.

nested_list = [1, 2, 3, [4, 5, 6, [7, 8, 9, 10, 11], 12, 13], 14, 15, [16, 17], 18, [19]]

def nested(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from nested(element)
        else:
            yield element

for element in nested(nested_list):
    print(element)


# List Comprehensions with Lambda Functions: Rewrite a traditional for loop that filters a list of numbers based
# on a specific condition using a list comprehension with a lambda function.

l1=[1,2,3]
l2=[4,5,6]
print([x*y for x in l1 for y in l2])