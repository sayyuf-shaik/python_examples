from ctypes import *

mylib = cdll.LoadLibrary("mylib.dll")


mylib.addnumbers.argtypes = [c_int, c_int]

mylib.addnumbers.restype = [c_int]

result = mylib.add_numbers(5, 7)
print(result)