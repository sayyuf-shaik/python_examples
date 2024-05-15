"""
Playing with dictionaries and their builtin methods

Dictionaries are key, value pairs, are indexed by keys.
keys can be anything that is immutable such as string, integer and tuples.
tuples which are having elements that are mutable cannot be used keys.
del keyword can be used to delete a key value pair

list(dict) would return a list of keys.
in operator can be used to check membership for keys.

"""

dict_1 = {"one": 1, "two": 2}

print(dict_1)
print(dict_1["one"])

print(list(dict_1))

del dict_1["one"]

print(dict_1)

if "two" in dict_1:
    print("yes")

# Merging two dictionaries into 1

dict_1 = {"one": 1, "two": 2}
dict_2 = {"three": 3, "four": 4}
dict_1.update(dict_2)
print(dict_1)

dict_2.clear()
print(dict_2)

# copy will shallow copy the dictionary
dict_0 = dict_1.copy()

print(dict_0)

# Get: Get will get the value of provided key
# Syntax: get(<key>, <default_value_to_return_if_not_found>)

print(dict_1.get("one", 0))

print(dict_1.get("five")) # doesnot raise KeyError and returns None

# Pop: pop will remove the key, value pair of provided key
# Syntax: pop(<key>, <default_value_to_return_if_not_found>)

print(dict_1.pop("one", 0))

print(dict_1.pop("five")) # will raise KeyError


# fromkeys()

