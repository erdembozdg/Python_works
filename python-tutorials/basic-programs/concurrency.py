
import time
from threading import Thread, Event
from contextlib import contextmanager

from queue import Queue
from threading import Thread, Lock

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n, evt):
        print('countdown starting')
        evt.set()
        while self._running and n>10:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

print("----------------")

def producer(out_q):
    data = b"erdem"
    while True:
        out_q.put(data)

def consumer(in_q):
    while True:
        data = in_q.get()
        print(data)

print("----------------")

class SharedCounter:
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = Lock()

    def inc(self):
        with self._value_lock:
            self._value += 1

    def decr(self):
        with self._value_lock:
            self._value -= 1


if __name__ == '__main__':
    evt = Event()
    c = CountdownTask()
    t = Thread(target=c.run, args=(10, evt))
    t.start()

    evt.wait()
    print('countdown running')
    c.terminate()
    if t.is_alive():
        print('Still running')
    else:
        print('Completed')
    t.join()

    # q = Queue()
    # t1 = Thread(target=consumer, args=(q, ))
    # t2 = Thread(target=producer, args=(q, ))
    # t1.start()
    # t2.start()



