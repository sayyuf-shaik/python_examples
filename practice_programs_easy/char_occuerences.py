string = 'aaaabbbbbcertttyyy'

occurences = {}
# Approach 1:
for char in set(string):
    occurences[char] = string.count(char)

print(occurences)

occurences = {}
# Approach 2:
prev_char = None
for char in string:
    if char != prev_char:
        occurences[char] = 1
    else:
        occurences[char] += 1
    prev_char = char
print(occurences)