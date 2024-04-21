#skonczone 
def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class Queue:
    def __init__(self, size = 5):
        self.array = [None for i in range(size)]
        self.size = size
        self.zid = 0
        self.oid = 0

    def length(self) -> int:
        return len(self.array)
    
    def is_empty(self) -> bool:
        if self.zid == self.oid:
            return True
        else:
            return False
        
    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.array[self.oid]
        
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            val = self.array[self.oid]
            self.oid = (self.oid + 1) % self.size
            return val
        
    def enqueue(self, val):
        self.array[self.zid] = val
        self.zid = (self.zid + 1) % self.size
        
        if self.zid == self.oid:
            self.array = realloc(self.array, 2 * self.size)
            old = self.size
            self.size = 2 * self.size
            new = self.size
            for i in range(self.oid, old):
                self.array[new- 1] = self.array[old - i]
                new -= 1
            self.oid = new

    def print_ar(self):
        result = "[" + " ".join(str(self.array[i]) for i in range(self.size)) + "]"
        return result
    
    def __str__(self):
        result = "["
        if self.zid >= self.oid:
            result += ' '.join(map(str, self.array[self.oid:self.zid]))
        else:
            result += ' '.join(map(str, self.array[self.oid:] + self.array[:self.zid]))
        result += "]"
        return result


def main():
    kolejka = Queue()

    for i in range(1,5):
        kolejka.enqueue(i)

    print(kolejka.dequeue())
    print(kolejka.peek())
    print(kolejka)
    for i in range(5,9):
        kolejka.enqueue(i)
    print(kolejka.print_ar())

    while not kolejka.is_empty():
        print(kolejka.dequeue())


    print(kolejka)

if __name__ == "__main__":
    main()