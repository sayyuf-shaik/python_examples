import os
new_list = []
for root, dir, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        size = os.path.getsize(file_path)
        new_list.append([size, file_path])

numbers = new_list
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j][0] > numbers[j + 1][0]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers[-1])
