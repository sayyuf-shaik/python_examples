"""
Polymorphism means having multiple forms.
"""


# Example:

class Bird:

    def intro(self):
        print("This is bird class")

    def flight(self):
        print("some of the birds can fly")

class Sparrow(Bird):

    def flight(self):
        print("Sparrow can fly")

class Ostrich(Bird):

    def flight(self):
        print("ostrich cannot fly")


# In the above example, the method flight() exists in different forms in different classes.
# This is classic example of polymorphism

sparrow = Sparrow()
sparrow.flight()

ostrich = Ostrich()
ostrich.flight()
