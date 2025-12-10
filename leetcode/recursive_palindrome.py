# check if a string is palindrome


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# print(is_palindrome("125421"))
# The sum digits


def sum_of_digits(number):

    if number < 10:
        return number

    return number % 10 + sum_of_digits(number//10)

print(sum_of_digits(1234))

