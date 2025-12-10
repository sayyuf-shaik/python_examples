class Employee():
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def _display(self):
        print(self._name, self._salary)


emp = Employee("sayyuf", "100000")
print(emp._name)
print(emp._salary)

print("+++++++++++++++++Private variables********************")

class Employee2():
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __display(self):
        print(self.__name, self.__salary)

    def public_display(self):
        self.__display()

obj = Employee2("sayyuf", "10000")
try:
    print(obj.__name)
    print(obj.__salary)
except Exception as e:
    print(e)

print(obj.public_display())
print(obj._Employee2__name)


class Employee3():
    def __init__(self):
        self.__name = None
        self.__salary = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name  = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

obj = Employee3()
obj.salary = 1000000
obj.name = "sayyuf"

print(obj.salary, obj.name)







