
input = {
    1: ['all', 'is'], 2: ['is', 'well'], 3: ["well", "all"]
    }

output = {'all': [1, 3], 'is': [1, 2], 'well': [2, 3]}
# Approach 1:
# create a list of all the values
# remove the duplicates in sorted order
# loop through key value pair and create a list and start appending the resp. key values
prev_value = None
values = []
for value in input.values():
    if prev_value != value:
        values.append(value)
    prev_value = value

prev_value = None
for key, value in input.items():
    for item in value:
        if prev_value != value:
            values.append(key)
        prev_value = value

