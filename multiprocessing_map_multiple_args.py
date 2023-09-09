import time
from multiprocessing import Pool, cpu_count
from functools import partial


def square(x, y):
    return x ** y


if __name__ == '__main__':
    num_process = cpu_count()
    print(f'cpu available {num_process}')
    l1 = [1, 2, 3]
    l2 = [4,5,6]

    start = time.time()

    with Pool(num_process) as pool:
        result = pool.starmap(square, zip(l1, l2))

    print(result)

    print(f'it took {time.time() - start} to complete')
