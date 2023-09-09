import threading
import time

x = 0


def thread_task(lock):
    global x
    for i in range(100000):
        lock.acquire()
        x += 1
        lock.release()


if __name__ == '__main__':
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'x = {x}')
