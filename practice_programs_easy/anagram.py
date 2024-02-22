"""
1. Anagram Finder:

Create a function that takes two words as input and checks if they are anagrams (have the same letters but different arrangements).
Handle case sensitivity and special characters as desired.
Example: is_anagram("inema", "iceman") should return True.
"""


def is_anagram(string1, string2):
    sorted_string1 = sorted(string1.lower())
    sorted_string2 = sorted(string2.lower())

    if "".join(sorted_string1) == "".join(sorted_string2):
        print("anagram")


is_anagram("$inema", "i$eman")