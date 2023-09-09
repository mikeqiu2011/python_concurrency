import time
from threading import Thread


def check_value_in_list(li):
    for i in range(10 ** 8):
        i in li


num_threads = 4
li = [1, 2, 3]

threads = []
start = time.time()

for i in range(num_threads):
    t = Thread(target=check_value_in_list, args=(li,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print(f'it took {time.time() - start} to complete')
