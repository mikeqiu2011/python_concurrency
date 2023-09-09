import threading
import time

x = 0


def thread_task():
    global x
    for i in range(10**6):
        x += 1


if __name__ == '__main__':
    threads = []

    for i in range(100):
        thread = threading.Thread(target=thread_task)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # t1 = threading.Thread(target=thread_task, args=(lock,))
    # t2 = threading.Thread(target=thread_task, args=(lock, ))
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

    print(f'x = {x}')
