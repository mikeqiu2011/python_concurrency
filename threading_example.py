import threading
import time


def print_epoch(thread_name, delay):
    for _ in range(3):
        time.sleep(delay)
        print(thread_name, '_' * 10, time.time())


if __name__ == '__main__':
    t1 = threading.Thread(target=print_epoch, args=('thread1', 1))
    t2 = threading.Thread(target=print_epoch, args=('thread2', 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('done')
