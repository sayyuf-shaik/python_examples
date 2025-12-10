"""
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“,
“]” are correct in exp.

Example:

Input: exp = “[()]{}{[()()]()}”
Output: Balanced

Input: exp = “[(])”
Output: Not Balanced
"""
# This problem can be solved with stack approach
# refer:
# https://www.geeksforgeeks.org/python-program-to-check-for-balanced-brackets-in-an-expression-well-formedness-using-stack/
# you can keep on pushing the last element to stack, compare top of the stack to the element is about to be pushed
# if top of the stack and current element to be pushed is same then, the list does not have balanced parenthis
# else balanced
# Approach 1:
# string = '[()]{}{[())]()}'

string = ')'

def check_balence(string):
    map_paren = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    # Step1: let us create a stack for the string
    stack = [] # [ '[',  ]
    # Step2: loop through the string and start pushing the element to stack
    for item in string:
        if item in map_paren.keys():
            stack.append(item)
        else:
            # stack might be empty if string has only closing brackets
            if not stack:
                return False
            for key, value in map_paren.items():
                if item == value and key == stack[-1]:
                    stack.pop()
                    break

            if len(stack) == 0:
                return True
            return False


if check_balence(string):
    print('Balanced')
else:
    print('Not balanced')

# Step3: Check if the top of stack and current element to be pushed should not be same.
# Step4: If same break the loop
# Approach 2:
stack = []

for char in string:
    if char in ('(', '[', '{'):
        stack.append(char)
    elif stack:
        if char not in ('(', '[', '{'):
            stack.pop()

print(stack)
if len(stack) == 0:
    print('Balanced')
else:
    print('Not balanced')



