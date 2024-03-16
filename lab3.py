class Queue:
    def __init__(self):
        self.array = [None for i in range(5)]
        self.size = self.length()
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
            self.array[self.oid] = None
            self.oid += 1
            return self.array[self.oid]
        
    def enqueue(self, val):
        self.array[self.zid] = val
        self.zid += 1
        #if self.oid == self.zid:
        #    self.realloc()

    def realloc(self, id):
        new_tab = [None for i in range(2*self.size)]
        new_tab[]
        self.array = new_tab
    
    def __str__(self):
        return f"[{self.array}]"


def main():
    kolejka = Queue()

    for i in range(1,5):
        kolejka.enqueue(i)

    print(kolejka)
    kolejka.dequeue()

if __name__ == "__main__":
    main()