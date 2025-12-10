import threading
import time


def sample(index):
    print("start thread ", index)
    time.sleep(2)
    print("end thread ", index)



if __name__ == '__main__':
    print("main thread")
    for index in range(3):
        thread = threading.Thread(target=sample, args=(index,))
        thread.start()
        thread.join()

