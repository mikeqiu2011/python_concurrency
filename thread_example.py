import _thread
import time


def print_epoch(thread_name, delay):
    for _ in range(3):
        time.sleep(delay)
        print(thread_name, '_' * 10, time.time())


_thread.start_new_thread(print_epoch, ('thread1', 1))
_thread.start_new_thread(print_epoch, ('thread2', 3))

input()