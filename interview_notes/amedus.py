string = "aabbccbbbaa"

prev = None

count = 0

for i in string:
    if prev == i:
        count += 1
    else:
        count = 0
    prev = i

print(count)