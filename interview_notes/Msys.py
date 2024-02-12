
def method():
    yield 1
    yield 2


for i in method():
    print(i)

list1 = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * x, list1)))


class Example:
    class_variable = "Class"

    def __init__(self, name):
        self.name = name

    def method(self):
        print("I am a method!")

    @classmethod
    def class_method(cls):
        print("class method")

    @staticmethod
    def static_method():
        print("Static method")


obj = Example("object")
obj.method()
obj.class_method()
obj.static_method()

Example("static").static_method()


class Child(Example):
    def __init__(self):
        super().__init__(Example)
        pass

    def method(self):
        super().method()
        print("I m a child method")


obj2 = Child()

obj2.method()

dict1 = {"one": 1, "two": 2, "three": 3, "four": 2, "five": 2, "six": 1}

values = list(dict1.values())

for item in set(values):
    print(item, values.count(item))

# i/p: "Hello How Are You Doing"

# o/p : "olleH woH erA uoY gnioD"

string = "Hello How Are You Doing"

rev_string = ""

for word in string.split():
    rev_string = rev_string + word[::-1] + " "

print(rev_string)

list1 = ["13", "16", "1", "5", "8"]

int_list1 = list(map(lambda x: int(x), list1))

for i in range(len(list1)):
    for j in range(i):
        if int_list1[i] < int_list1[j]:
            int_list1[i], int_list1[j] = int_list1[j], int_list1[i]

list1 = list(map(lambda x: str(x), int_list1))

print(list1)

list_big = [10, 5, 8, 20, 3, 19]

for i in range(len(list_big)):
    for j in range(i):
        if list_big[i] < list_big[j]:
            list_big[i], list_big[j] = list_big[j], list_big[i]

print(list_big[-2])






