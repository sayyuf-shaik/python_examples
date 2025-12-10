"""
A decorator is concept, where one can add a functionality into the function/method without modifying the existing
function

Example: Adding a timer to a function/method.

"""
import time


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Duration:", end - start)
    return inner


@timer
def just_sleep(time_to_sleep):
    time.sleep(time_to_sleep)


just_sleep(5)





