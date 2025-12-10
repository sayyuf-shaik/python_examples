list1 = [1,2,2,'a','a','s','s',2,3,4]

revlist = list1[::-1]

for i in range(len(list1)-1, -1, -1):
    # If the current element appears earlier in the list, remove it
    if list1[i] in list1[:i]:
        del list1[i]

print(list1)




print(list1)
