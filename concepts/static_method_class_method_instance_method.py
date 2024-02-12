"""
An Instance method will be having a self as first arguments and will be bound to the instance of the object
An instance method can access class variables and instance variables

Class method will be having a cls as first argument and will be bound to class.
Class method can only be able to access class variables

Static method doesn't have any arguments and will not be bound to either class or object
A static method cannot access the class variables and instance variables.

A method only be used a class method when all the variables are class variables.
"""

class Example:
    class_variable = "Class"

    def __init__(self, name):
        self.name = name

    def method(self): # This is an instance method
        print("I am a method!")
        print(self.class_variable)  # you can access the class variable using cls
        print(self.name)

    @classmethod
    def class_method(cls):
        """
        Class method
        :return:
        """
        print(cls.class_variable) # you can access the class variable using cls

        # This will result in an attribute since cls cannot access the instance variable
        try:
            print(cls.name)
        except AttributeError as attr_error:
            print("AttributeError: ", attr_error)
        print("class method")

    @staticmethod
    def static_method():
        """
        Static method
        :return:
        """
        print("Static method")


obj = Example("object")
obj.method()
obj.class_method()
obj.static_method()

# Static method can be called using the class name
Example.static_method()
# Class method also can be called using the class name
Example.class_method()

# Instance method can only be accessed using object that is intialized to the class
# this will result in a type error
try:
    Example.method()
except TypeError as type_error:
    print("Type Error: ", type_error)
