"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# Approach
# s = "c"
# Get all the substrings in an given string
"""
o find all possible substrings of the string s = "abcabcbb", we can generate all contiguous sequences of characters within the string. Here's how you can do it:

Step-by-Step Approach:
Understand what a substring is: A substring is a contiguous sequence of characters within a string. For example, in "abc", the substrings are "a", "b", "c", "ab", "bc", and "abc".

Generate all possible substrings:

For a string of length n, there are n*(n+1)/2 possible substrings.

We can generate substrings by fixing a starting index and then varying the ending index from the starting index to the end of the string.

Substrings of "ABCpdf":
The string "abcabcbb" has a length of 8, so there are 8*9/2 = 36 possible substrings.

Let's list them:

Length 1:

"a", "b", "c", "a", "b", "c", "b", "b"

Length 2:

"ab", "bc", "ca", "ab", "bc", "cb", "bb"

Length 3:

"abc", "bca", "cab", "abc", "bcb", "cbb"

Length 4:

"abca", "bcab", "cabc", "abcb", "bcbb"

Length 5:

"abcab", "bcabc", "abcbb"

Length 6:

"abcabc", "bcabcb"

Length 7:

"abcabcb"

Length 8:

"abcabcbb"

Complete List of All Substrings:
Here is the exhaustive list of all 36 substrings:

"a"

"b"

"c"

"a"

"b"

"c"

"b"

"b"

"ab"

"bc"

"ca"

"ab"

"bc"

"cb"

"bb"

"abc"

"bca"

"cab"

"abc"

"bcb"

"cbb"

"abca"

"bcab"

"cabc"

"abcb"

"bcbb"

"abcab"

"bcabc"

"abcbb"

"abcabc"

"bcabcb"

"abcabcb"

"c"

Note:
Some substrings are repeated (e.g., "a", "b", "c", "ab", "bc", "abc" appear multiple times).

The total number of unique substrings is less than 36 due to duplicates. If you want only unique substrings, you can remove the duplicates from the list above.
"""


def longestUniqueSubstr(s):
    charSet = set()

    l = 0
    result = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        result = max(result, r - l + 1)
    return result


# longestUniqueSubstr("")


# print(obj.lengthOfLongestSubstring("abcabcb"))
print(longestUniqueSubstr("abcabcb"))
