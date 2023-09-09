import time
from multiprocessing import Process


def check_value_in_list(li):
    for i in range(10 ** 8):
        i in li


if __name__ == '__main__':
    num_process = 4
    li = [1, 2, 3]

    processes = []
    start = time.time()

    for i in range(num_process):
        process = Process(target=check_value_in_list, args=(li,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print(f'it took {time.time() - start} to complete')
