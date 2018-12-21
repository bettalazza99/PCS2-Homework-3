import matplotlib.pyplot as plt
import random, time, heapq
class MinMaxBubble(object):
    def __init__(self):
        self.content = []

    def bubble_sort(self):
        for passnum in range(len(self.content)-1,0,-1):
            for i in range(passnum):
                if self.content[i]>self.content[i+1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i+1]
                    self.content[i + 1] = temp
    def add(self,value):
        self.content.append(value)
        self.bubble_sort()

    def get_min(self):
        return self.content[0]
    def get_max(self):
        return self.content[-1]


m= MinMaxBubble()
m.add(2)
m.add(5)
m.add(4)
m.add(12)
print(m.get_max())
print(m.get_min())
print(m.bubble_sort())

import random
import matplotlib.pyplot as plt
for r in range(100):
    num = random.randint(0,1000)
    m.add(num)
    my_min = m.get_min()
    my_max = m.get_max()

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
    m = MinMaxBubble()
    m.add(5)
    print(m.content, m.get_min(), m.get_max())
    m.add(7)
    print(m.content, m.get_min(), m.get_max())
    m.add(3)
    print(m.content, m.get_min(), m.get_max())
    m.add(9)
    print(m.content, m.get_min(), m.get_max())

    repetitions = 3
    max_operations = 500
    step= 100

    values_bubble, values_bubble_min, values_bubble_max = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 500))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(5):
            a = MinMaxBubble()
            my_add, my_min, my_max = measure_time(a, this_list)
            tot_time_add += my_add
            tot_time_min += my_min
            tot_time_max += my_max

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_bubble.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        values_bubble_max.append(tot_time_max * 1000)

    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, values_bubble,color='b', linestyle='-',label='Add')
    plt.plot(xlabels, values_bubble_min,color='g', linestyle='--', label='Get Min')
    plt.plot(xlabels, values_bubble_max,color='y', linestyle='-.', label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Bubble's Solution")
    plt.show()
