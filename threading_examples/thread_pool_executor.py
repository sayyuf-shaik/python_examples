import concurrent.futures
import time


def sample(index):
    print("Thread Started", index)
    time.sleep(2)
    print("Thread Ended", index)






if __name__ == '__main__':

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(sample, range(4))