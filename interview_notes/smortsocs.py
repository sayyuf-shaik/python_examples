# factorial using generator
def product(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
        yield product

for i in product(5):
    print(i)