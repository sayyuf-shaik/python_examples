from abc import ABC, abstractmethod

class A(ABC):
    __abstract__ = True

    def __init__(self):
        pass

    @abstractmethod
    def method(self):
        raise NotImplemented


class B(A):

    def __init__(self):
        super().__init__()

    def method2(self):
        print("method2")



b = B()

b.method()
# what is data abstraction. one of the pillars of the OOPS concept
# hiding not necessary implmentation detials to the user
# implemented using ABC class

class Animal(ABC):

    @abstractmethod    # abstact method
    def make_sound(self):
        pass

    def sleep(self): #concrete method
        print("Zzzzzz")

class Bird(Animal):

    def make_sound(self):
        print("Chirp")

class Dog(Animal):

    def make_sound(self):
        print("Bark")







