from threading import Thread
from multiprocessing import Process, cpu_count
import os
import time

# class InputReader(Thread):
#     def run(self):
#         self.text = input()

# print("Enter some text: ")
# thread = InputReader()
# thread.start()

# counter = 1

# while thread.is_alive():
#     counter += 1

# print(counter, thread.text)


class MuchCPU(Process):
    def run(self):
        print(os.getpid())
        for i in range(200000):
            pass


if __name__ == '__main__':
    procs = [MuchCPU() for x in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()

    for p in procs:
        p.join()

    print("work took {}".format(t - time.time()))