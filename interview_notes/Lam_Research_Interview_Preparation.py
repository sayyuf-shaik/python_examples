"""
Polymorphism and written examples, puzzles, even or odd number without using mod
Code snippet, Two Sum, Star printing pattern, Problems on Linkedlist, Puzzles, Project explanation, OS, OOPS questions. I

HashMap
"""
import os

main_dict = {}

def insert(item):
    if item in main_dict:
        main_dict[item] += 1
    else:
        main_dict[item] = 1
    # print(main_dict)

insert("key1")
insert("key2")
insert("key2")
insert("key3")
insert("key1")

# print(len(main_dict))


pat = [1, 2, 0, 3, 2, 2, 3, 0]

for p in pat:
    pass
    if p == 0:
        current = p
        break
    elif p % 2 == 0:
        continue
    # print(p)

# print(current)

temp = 10

def func():
    global temp
    temp = 20
    print(temp)
print(temp)
func()
print(temp)


for (root, dir, files) in os.walk("../interview_notes"):
    for file in files:
        if file.startswith("Lam"):
            print(file)


string = "sayyuf"
new_text = ""

for char in string:
    if char not in ("a", "e", "i", "o", "u"):
        new_text += char

print(new_text)



