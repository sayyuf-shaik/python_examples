# A generator is function/method that contains atleast one yield statement.
# A normal function/method returns the control every time but yiels stores the state of the function and resumesa afte


# def get_numbers_list(n):
#     new_list = []
#     for i in range(len(n)):

original = {"a": 1, "b": 2, "c": 3}
new_dict = {}

for key, value in original.items():
    new_dict[value] = key

print(new_dict)

# Merge two dictionaries
another = {'d': 4, 'e': 5}

new_dict = dict()
scores = {"Alice": 85, "Bob": 60, "Charlie": 72, "Dave": 90}

print({key:value for key, value in scores.items() if value > 60})

sentence = "the quick brown fox jumps over the lazy dog"

new_dict = {}
for word in sentence.split():
    if word not in new_dict:
        new_dict[word] = 1
    else:
        new_dict[word] +=1
print(new_dict)

# Find out the biggest value of the key
sales = {"Apple": 120, "Banana": 80, "Cherry": 200}


values = list(sales.values())

biggest = values[0]

for i in values:
    if i > biggest:
        biggest = i

for key, value in sales.items():
    if value == biggest:
        print(key, value)

sales = {"Apple": 120, "Banana": 80, "Cherry": 200}
new_dict = {}
values = list(sales.values())

for i in range(len(values)):
    for j in range(len(values) - 1):
        if values[j] > values[j+1]:
            values[j], values[j + 1] = values[j+1], values[j]
print(values)
for item in values:
    for key, value in sales.items():
     if item == value:
         new_dict[key] = item

print(new_dict)


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}

for key,value in dict2.items():
    if key in dict1:
        print(key)

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 25}
]

original = {"a": 1, "b": 2, "c": 1}

new_dict = {}

for key, value in original.items():
    if value in new_dict:
        new_dict[value].append(key)
    else:
        new_dict[value] = [key]

print(new_dict)


# String Operations
s = "hello"

new_list = ''

for i in range(len(s) - 1, -1, -1):
    new_list = new_list + s[i]

print(new_list)

list_1 = [1, 2, 3, 4, 5]

new_list = []

for i in list_1:
    new_list.insert(0, i)

print(new_list)

# Problem 2: Find the Second Largest Number in a List
numbers = [10, 5, 20, 15]

for i in range(len(numbers)):
    for j in range(len(numbers) -1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers[-2])
# Problem 3: Remove All Occurrences of a Value
my_list = [1, 2, 3, 2, 4, 2, 5]

# for i in my_list:
#     if i == 2:
#         my_list.remove(2)
#
# print(my_list)

print([x for x in my_list if 2 != x])

# Problem 4: Rotate a List by n Positions
my_list = [1, 2, 3, 4, 5]

new_list = my_list[4:] + my_list[:4]
print(new_list)
# Problem 5: Flatten a Nested List (Recursively)

nested = [1, [2, [3, 4], 5]]

def flatten(nested):
    for item in nested:


