import time
from multiprocessing import Pool, cpu_count
from functools import partial


def square(y, x):
    return x ** y


power = 3
partial_func = partial(square, power)

if __name__ == '__main__':
    num_process = cpu_count()
    print(f'cpu available {num_process}')
    li = [1, 2, 3]

    start = time.time()

    with Pool(num_process) as pool:
        result = pool.map(partial_func, li)

    print(result)

    print(f'it took {time.time() - start} to complete')
