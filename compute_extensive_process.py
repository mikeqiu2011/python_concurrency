import time
from multiprocessing import Process, Queue

max_num_to_check = 10 ** 9
queue = Queue()


def check_value_in_list(li, i, num_of_process, queue):
    num_of_hits = 0
    lower = int(i * max_num_to_check / num_of_process)
    upper = int((i + 1) * max_num_to_check / num_of_process)

    for i in range(lower, upper):
        if i in li:
            num_of_hits += 1

    queue.put((lower, upper, num_of_hits))


if __name__ == '__main__':
    num_process = 4
    li = [1, 10**6, 10**7]

    processes = []
    start = time.time()

    for i in range(num_process):
        process = Process(target=check_value_in_list, args=(li, i, num_process, queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    queue.put('DONE')

    while True:
        message = queue.get()
        if message == 'DONE':
            break

        print(message)

    print(f'it took {time.time() - start} to complete')
