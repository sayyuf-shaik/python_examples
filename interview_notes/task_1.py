# 1. generate list of 10 random integers from 1 to 10 and call it "rand_10"
import random

rand_10 = [random.randint(1, 10) for i in range(10)]
print(rand_10)
# 2. in a loop iterate by "rand_10" items and store each item in a new line in file "rand_10.txt"
with open("rand_10.txt", "w") as fp:
    for rand_element in rand_10:
        fp.write(str(rand_element) + "\n")
# 3. write a function which will take "rand_10" as input and then will return each second element.
#
# function should print how many items was on input list and how many on output list
#
# execute this function and print output


def get_each_second_element(input_list):
    output_list = input_list[1::2]
    print(f"The number of items in the input list is: {len(input_list)}")
    print(f"The number of items in the output list is: {len(output_list)}")
    return output_list

print("Every Second consecutive element in the list", get_each_second_element(rand_10))

# 4. read values from "rand_10.txt" file into dictionary,
#
# where key is a number of a row (line from file) and value is a content of this row

random_dict = dict()
with open("rand_10.txt") as fp:
    lines = fp.readlines()
    for index, line in enumerate(lines):
        random_dict[index + 1] = line.strip("\n")

print(random_dict)

# 5. iterate by dictionary and print all items if theirs key is divisible by 3
for key, value in random_dict.items():
    if key % 3 == 0:
        print(f"{key}: {value}")