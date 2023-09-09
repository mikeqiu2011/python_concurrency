import time
from multiprocessing import Pool, cpu_count


def square(x):
    return x ** 2


if __name__ == '__main__':
    num_process = cpu_count()
    print(f'cpu available {num_process}')
    li = [1, 2, 3]

    start = time.time()

    with Pool(num_process) as pool:
        result = pool.map(square, li)

    print(result)

    print(f'it took {time.time() - start} to complete')
