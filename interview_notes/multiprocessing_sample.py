from multiprocessing import Process


def worker(name):
    print("Name of the worker", name)


if __name__ == '__main__':
    process = []

    for i in range(5):
        p = Process(target=worker, args=(i,))
        process.append(p)
        p.start()

    for p in process:
        p.join()