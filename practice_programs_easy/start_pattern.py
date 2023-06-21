# """
# *
# * *
# * * *
# * * * *
# * * * * *
# """
# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print('*', end="")
#     print()
#
# """
# * * * * *
# * * * *
# * * *
# * *
# *
# """
# for i in range(n):
#     for j in range(n - i):
#         print('*', end="")
#     print(
#     )
#
# """
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# """
# for i in range(n):
#     print(' ' * (n - 1 - i), end="")
#     for j in range(i + 1):
#         print('*', end="")
#     print()
"""
    *
   * *
  * * *
 * * * *
* * * * *

"""


def triangle(n):
    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


n = 5
k = n - 1

# for i in range(0, n):
#     for j in range(0, k):
#         print(end=' ')
#
#     k -= 1
#     for j in range(0, i + 1):
#         print("* ", end='')
#     print("\r")
#
#
# triangle(5)
"""
 0 1 2 3 4
0    *
1  * * * 
2* * * * *
3  * * * 
4    * 
"""

def daimond(n):
    k = n
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k = k // 2

        for j in range(i + 1):
            print("*", end=" ")
        print("")

daimond(5)











