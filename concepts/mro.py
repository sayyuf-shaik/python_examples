"""
how a child classes are inherited, when there are two or more classes are being inherited.
which parent class will first get inherited? which order?
"""


class A:
    def __init__(self):
        self.name = "class A"

    def method(self):
        print('Im method inside a class A')


class B:
    def __init__(self):
        self.name = "class B"

    def method(self):
        print('Im method inside a class B')


"""
The MRO the method resolution order would be from left to right i.e what first class you've mentioned in you're child
class
in the below case i.e B. Python tries to find the attribute in the B class first if found B method would be called
If not then Method from A class would be called.
"""


class C(A, B):
    def __init__(self):
        super().__init__()
        self.name = "class C"

    def c_method(self):
        print('Im method inside a class A')

obj = C()

obj.method()

