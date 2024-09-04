import random
import time
from copy import deepcopy

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
    
def  insertSort(tab):
    for i in range(len(tab)):
        j = i
        while j > 0 and tab[j] < tab[j-1]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j -= 1
    return tab

def shellSort(tab, h = None):
    if h == None:
           h = len(tab) // 2

    while h > 0:
        for i in range(h, len(tab)):
            j = i
            while j - h >= 0 and tab[j] < tab[j-h]:
                tab[j], tab[j-h] = tab[j - h], tab[j]
                j -= h
        h = h // 2
    return tab

def main():
    elem = [ Element(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    elem2 = deepcopy(elem)

    print(insertSort(elem))
    print(shellSort(elem2))

    t = [int(random.random() * 100) for _ in range(10000)]
    t2 = deepcopy(t)

    t_start1 = time.perf_counter()
    insertSort(t)
    t_stop1 = time.perf_counter()
    print("Metoda przez wstawianie:",
          "{:.7f}".format(t_stop1 - t_start1))
    
    t_start2 = time.perf_counter()
    shellSort(t2)
    t_stop2 = time.perf_counter()
    print("Metoda Shella:",
          "{:.7f}".format(t_stop2 - t_start2))

if __name__ == '__main__':
    main()