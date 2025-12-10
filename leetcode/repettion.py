string = "abcabcba"

charset = set()
l = 0
result = 0

for r in range(len(string)):
    while string[r] in charset:
        charset.remove(string[l])
        l += 1
    charset.add(string[r])
    result = max(result, r-l+1)

print(result)
