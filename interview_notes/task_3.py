# Write a piece of code, to catch both values (not mem addr or offset),
# convert them from string to a number , and compare which one is greater
import re
string = "MSR bank addr 0x432FCD00 value is 0xDEADBEAF007, while including offset 0x2137 value is" \
         " 0b11011110101011011011111010101111000000000111"

numbers = re.findall(r"value is ([0-9A-Za-z]+)", string)

number_1 = int(numbers[0], 16)
number_2 = int(numbers[1], 2)

# print(number_1)
# print(number_2)

if number_1 > number_2:
    print(f"{number_1} is greater")
elif number_1 == number_2:
    print(f"{number_1} and {number_2} are equal")
else:
    print(f"{number_2} is greater")

