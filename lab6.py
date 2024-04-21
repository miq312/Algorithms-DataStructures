class Element:
    def __init__(self, data, priorytet):
        self.data = data
        self.priorytet = priorytet

    def __repr__(self):
        return f"{self.priorytet} : {self.data}"

    def __gt__(self, other):
        return self.priorytet > other.priorytet

    def __lt__(self, other):
        return self.priorytet < other.priorytet


class Heap:
    def __init__(self):
        self.tab = []

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

    def repair(self, start):
        left = self.left(start)
        right = self.right(start)
        max = start

        if left <= self.size - 1 and self.tab[left] > self.tab[max]:
            max = left

        if right <= self.size - 1 and self.tab[right] > self.tab[max]:
            max = right

        if max != start:
            self.tab[start], self.tab[max] = self.tab[max], self.tab[start]
            self.repair(max)

    def enqueue(self, element: Element):
        self.tab.append(element)
        curr = self.size - 1

        while curr > 0 and self.tab[curr] > self.tab[self.parent(curr)]:
            self.tab[curr], self.tab[self.parent(curr)] = self.tab[self.parent(curr)], self.tab[curr]
            curr = self.parent(curr)

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

def main():

    queue = Heap()
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    dane = "GRYMOTYLA"

    for i in range(len(priorytety)):
        queue.enqueue(Element(dane[i],priorytety[i]))

    queue.print_tree(0,0)
    queue.print_tab()
    pierwszy = queue.dequeue()
    print(pierwszy)
    print(queue.peek())
    queue.print_tab()
    print(pierwszy)
    while not queue.is_empty():
        print(queue.dequeue())
    
    queue.print_tab()

if __name__ == '__main__':
    main()