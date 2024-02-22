# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")

# get('key', None)

# pop()

# {"one":1} + {"two": 2} = {"one": 1, "two": 2}

# [("one", 1)] +[("two", 2)] =

# [("one", 1), ("two", 2)]

# sys.argv[0], sys.argv[1]


# argparser

# --help,
# -filename , action=

# @classmethod


# @staticmethod


# input = {"vjw": "ap", "vsp": "ap", "bng": "ka", "chn": "tn", "cmb": "tn", "mys": "ka", "hyd": "tg", "tpt": "ap"}

# output={"ap": ["vjw", "vsp", "tpt"], "ka": ["blr", "mys"], "tg": ["hyd"], "tn": ["chn", "cmb"]}


input_dict = {"vjw": "ap", "vsp": "ap", "bng": "ka", "chn": "tn", "cmb": "tn", "mys": "ka", "hyd": "tg", "tpt": "ap"}

new_dict = {}

for key, value in input_dict.items():
    if value in new_dict:
        new_dict[value].append(key)
    else:
        new_dict[value] = [key]

print(new_dict)

# input = "television"

# Out1= "tlvson"
# Out2 = "ei"

input_string = "television"

out1 = ""
out2 = ""

for char in input_string:
    count = 0
    for index in range(len(input_string)):
        if char == input_string[index]:
            count += 1
    if count == 1:
        out1 = out1 + char
    elif char not in out2:
        out2 = out2 + char

print(out1)
print(out2)

import re

# Input = "1234 56 78 22 9 4567 0 00"
input_string = "1234 56 78 22 9 4567 0 00"

print(re.findall(r"\b[0-9]{2}\b", input_string))


class ABC:

    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30


class BCD(ABC):
    def __init__(self):
        self.a = 11
        self._b = 21
        self.__c = 31


bcd = BCD()
print(dir(bcd))

print(bcd.a)
print(bcd._b)
print(bcd._BCD__c)
















































