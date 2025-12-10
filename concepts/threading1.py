import time
import threading


def do_some_worker():
    print("sleeping for 20 secs")
    time.sleep(20)


def print_abcd():
    list_1 = ['a', 'b', 'c', 'd', 'e']
    for i in list_1:
        print(i)


thread1 = threading.Thread(target=do_some_worker)
thread2 = threading.Thread(target=print_abcd)

thread1.start()

thread2.start()

thread1.join()
thread2.join()


