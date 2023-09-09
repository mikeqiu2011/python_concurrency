import threading
import time

x = 0


def thread_task():
    global x
    for i in range(10):
        x += 1


if __name__ == '__main__':
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'x = {x}')
