class A:
    def __init__(self):
        self._name = "name"
        self.__id = "pass"

    def sample_method(self):

        print(self._name, self.__id)


obj = A()

obj.sample_method()

print(dir(obj))

print(obj._name)

obj._name = "fuck"
print(obj._name)

obj._A__id = "screwed"
print(obj._A__id)