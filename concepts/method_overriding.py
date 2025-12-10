"""
method overriding is an ability of an object-oriented programming language that allows a subclass or child class to have
a method with same as of parent class.
"""


class Parent:

    def __init__(self):
        self.name = "Parent class"

    def method(self):
        print(self.name)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = "child class"

    def method(self):
        print(self.name)


obj2 = Child()
obj2.method()
