import heapq
import matplotlib.pyplot as plt

class MinMaxHeap(object):
    def __init__(self):
        self.content_min=[]
        self.content_max=[]

    def add(self, value):
       heapq.heappush(self.content_min, value)
       heapq.heappush(self.content_max, -value)
    def get_max(self):
        return -self.content_max[0]
    def get_min(self):
        return self.content_min[0]


b = MinMaxHeap()

import random
for r in range(100):
    num = random.randint(0,1000)
    b.add(num)
    my_min = b.get_min()
    my_max = b.get_max()

import time


def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


if __name__ == '__main__':
    a = MinMaxHeap()
    a.add(5)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(7)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(3)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(9)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())

    repetitions = 5
    max_operations = 20000
    step = 5000

    values_heap_add, values_heap_min, values_heap_max = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 20000))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0

        for repetition in range(5):
           a = MinMaxHeap()
           myadd, mymin, mymax = measure_time(a, this_list)
           tot_time_add += myadd
           tot_time_min += mymin
           tot_time_max += mymax

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        values_heap_max.append(tot_time_max * 1000)



    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, values_heap_add,color='g', linestyle='-', label='Add')
    plt.plot(xlabels, values_heap_min,color='r', linestyle='--', label='Get Min')
    plt.plot(xlabels, values_heap_max,color='y', linestyle='-.', label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of HeapSort's Solution")
    plt.show()
