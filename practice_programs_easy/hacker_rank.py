#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    new_grades = []
    # Write your code here
    if 1 >= len(grades) >= 60:
        return

    for grade in grades:
        if 0 >= grade >= 100:
            return
        if grade < 38:
            new_grades.append(grade)
            continue
        grade_divisible = grade
        while grade_divisible <= 100:
            if grade_divisible % 5 == 0:
                if grade_divisible - grade < 3:
                    new_grades.append(grade_divisible)
                    break
                else:
                    new_grades.append(grade)
                    break
            grade_divisible += 1

    print(new_grades)
    return new_grades


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = 4

    grades = [73, 67, 38, 33]


    result = gradingStudents(grades)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
