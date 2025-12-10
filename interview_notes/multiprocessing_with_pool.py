from multiprocessing import Pool


def square(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        result = p.map(square, [1, 2, 3, 4, 5])
        print(result)