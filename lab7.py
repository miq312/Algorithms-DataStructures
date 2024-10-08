import random
import time
from copy import deepcopy
from typing import List

class Element:
    def __init__(self, priorytet, data):
        self.data = data
        self.priorytet = priorytet

    def __repr__(self):
        return f"{self.priorytet} : {self.data}"

    def __gt__(self, other):
        return self.priorytet > other.priorytet

    def __lt__(self, other):
        return self.priorytet < other.priorytet


class Heap:
    def __init__(self, tab):
        if tab == None:
            self.tab = []
        else:
            self.tab = tab

    def right(self, i):
        return 2 * i + 2

    def left(self, i):
        return 2 * i + 1

    def parent(self, i):
        return (i - 1) // 2
    
    @property
    def size(self):
        return len(self.tab)
    
    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        first = self.tab[0]
        self.tab[0] = self.tab[-1]
        self.tab = self.tab[:-1]

        self.repair(0)
        return first

    def createHeap(self):
        for i in range(self.size, -1, -1):
            self.repair(i, self.size)

    def repair(self, start, size):
        left = self.left(start)
        right = self.right(start)
        max = start

        if left <= size - 1 and self.tab[left] > self.tab[max]:
            max = left

        if right <= size - 1 and self.tab[right] > self.tab[max]:
            max = right

        if max != start:
            self.tab[start], self.tab[max] = self.tab[max], self.tab[start]
            self.repair(max, size)

    def enqueue(self, element: Element):
        self.tab.append(element)
        curr = self.size - 1

        while curr > 0 and self.tab[curr] > self.tab[self.parent(curr)]:
            self.tab[curr], self.tab[self.parent(curr)] = self.tab[self.parent(curr)], self.tab[curr]
            curr = self.parent(curr)

    def heapsort(self):
        for i in range(self.size - 1, -1, -1):
            self.tab[i], self.tab[0] = self.tab[0], self.tab[i]
            self.repair(0, i)

    def print_tab(self):
        if self.is_empty():
            print("{ }")
            return
        print('{', end=' ')
        for i in range(self.size - 1):
            print(self.tab[i], end=', ')
        if self.tab[self.size - 1]:
            print(self.tab[self.size - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

def firstTest():
    elem = [ Element(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    h = Heap(elem)
    h.createHeap()
    h.print_tab()
    h.print_tree(0,0)
    h.heapsort()
    h.print_tab()

def secondTest():
    randomNumbers = [int(random.random()*100) for i in range(1000)]
    h = Heap(randomNumbers)

    t_start = time.perf_counter()
    h.createHeap()
    h.heapsort()
    t_stop = time.perf_counter()
    print("Czas obliczeń: kopcowanie: ", "{:.7f}".format(t_stop - t_start))

def swap(tab):
    for i in range(len(tab)):
        k = tab[i]
        kId = i
        for  j in range(i, len(tab)):
            if k > tab[j]:
                kId = j
                k = tab[j]
        tab[i], tab[kId] = tab[kId], tab[i]
    return tab

def shift(tab):
    for i in range(len(tab)):
        k = tab[i]
        kId = i
        for j in range(i+1, len(tab)):
            if k > tab[j]:
                kId = j
                k = tab[j]
        elem = tab.pop(kId)
        tab.insert(i, elem)
    return tab

def main():
    firstTest()
    secondTest()
    
    elem = [ Element(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    elem2 = deepcopy(elem)

    print(shift(elem))
    print(swap(elem2))

    l = [int(random.random() * 100) for _ in range(10000)]
    t_start1 = time.perf_counter()
    shift(l)
    t_stop1= time.perf_counter()
    print("Czas obliczeń:przesunięcie elementów (shift):",
          "{:.7f}".format(t_stop1 - t_start1))

    l = [int(random.random() * 100) for _ in range(10000)]
    t_start2 = time.perf_counter()
    swap(l)
    t_stop2 = time.perf_counter()
    print("Czas obliczeń: zamiania miejscami (swap):",
          "{:.7f}".format(t_stop2 - t_start2))

if __name__ == '__main__':
    main()