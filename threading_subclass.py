import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self) -> None:
        print(f'start {self.name}')
        self.print_epoch()
        print(f'end {self.name}')

    def print_epoch(self):
        for _ in range(3):
            time.sleep(self.delay)
            print(self.name, '_' * 10, time.time())


if __name__ == '__main__':
    t1 = MyThread('thread1', 1)
    t2 = MyThread('thread2', 2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('done')
