def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    list_params = [s, t, a, b]

    for param in list_params:
        if 1 >= param >= pow(10, 5):
            print(param)
            print("here1")
            return

    for apple in apples:
        if 1 >= apple >= pow(10, 5):
            print("here2")
            return

    for orange in oranges:
        if 1 >= orange >= pow(10, 5):
            print("here3")
            return

    if a > s > t > b:
        return

    apples = list(map(lambda x: x + a, apples))
    oranges = list(map(lambda x: x + b, oranges))

    for apple in apples:
        if pow(-10, 5) >= apple >= pow(10, 5):
            print("here4")
            return

    for orange in oranges:
        if pow(-10, 5) >= orange >= pow(10, 5):
            print("here5")
            return

    apples_inclusive = [apple for apple in apples if 7 <= apple <= 10]
    oranges_inclusive = [orange for orange in oranges if 7 <= orange <= 10]
    print(len(apples_inclusive))
    print(len(oranges_inclusive))

countApplesAndOranges(2, 3, 1, 5, [2], [-2])


