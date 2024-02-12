"""
In python = Assignment operator does not copy the objects rather links the references of the objects to the new
variable.
Example:
    a = 5
    b = 5
    id(a) and id(b) both will have same reference as both are pointing to the same object i.e "5"

A Shallow copy will copy the top level structure and retains the low level child objects references. which means nested
children such as nested lists inside list will be referenced rather copied independently.
"""

# Shallow copy
import copy
list_1 = [1, 2, [3, 4], 5]
list_2 = copy.copy(list_1)

# updated the nested list value
list_2[2][0] = 7
# now print the copied the list
print(list_2)
# print the original list
# The value will get reflected in both the lists
print(list_1)

# Note: only nested objects Or child objects references will be retained where as the parent objects will be created
# independently

# change the value of the parent object
list_2[0] = 7
# now print the copied the list
print(list_2)
# print the original list
# The value will not get reflected in both the lists
print(list_1)

"""
A deep copy will create an independent structure by recurring through all the elements or child objects.
In simple terms no changes in the copied list will be reflected in the original list.

"""

# Deep copy
import copy
list_1 = [1, 2, [3, 4], 5]
list_2 = copy.deepcopy(list_1)

# updated the nested list value
list_2[2][0] = 7
# now print the copied the list
print(list_2)
# print the original list
# The value will not get reflected in both the lists
print(list_1)

# Note: only nested objects Or child objects references will be retained whereas the parent objects will be created
# independently

# change the value of the parent object
list_2[0] = 7
# now print the copied the list
print(list_2)
# print the original list
# The value will not get reflected in both the lists
print(list_1)
