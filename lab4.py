class Element():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return f"{self.key} : {self.value}"
    
class HashTable():
    def __init__(self, size, c1 = 1, c2 = 0):
        self.array = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2
    
    def hash(self, key):
        if type(key) == str:
            key = sum(ord(char) for char in key)
        return key % self.size

    def search(self, key):
        id = self.hash(key)
        i = 0
        while i < self.size:
            if self.array[id] != None and self.array[id].key == key:
                return self.array[id].value
            i += 1
            id = self.collision(key, i)
        return None
    
    def insert(self, key, value):
        i = 0
        while i < self.size:
            id = self.collision(key, i)
            if self.array[id] == None:
                self.array[id] = Element(key,value)
                return
            elif self.array[id].key == key:
                self.array[id].value = value
                return
            i += 1
        print("Brak miejsca")

    def remove(self, key):
        id = self.hash(key)
        i = 0
        while i < self.size:
            if self.array[id] != None and self.array[id].key == key:
                self.array[id] = None
                return
            i += 1
            id = self.collision(key,i)
        print("Brak danej")
    
    def collision(self, key, i):
        id = self.hash(key)
        return (id + self.c1 * i + self.c2 * i ** 2) % self.size

    def __str__(self):
        res = []
        for i in self.array:
            if i is None:
                res.append("None")
            else:
                res.append(str(i))
        return "{" + ", ".join(res) + "}"

def first_test(size, c1=1, c2=0):

    tab = HashTable(size,c1,c2)

    for i in range(1,16):
        key = i
        if key == 6: key = 18
        elif key == 7: key = 31
        tab.insert(key,chr(i+64))

    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5,'Z')
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    tab.insert('test', 'W')
    print(tab)

def second_test(size, c1=1, c2=0):
    tab = HashTable(size,c1,c2)
    for i in range(1, 16):
        tab.insert(i*13, chr(i + 64))
    print(tab)

def main():
    print("\n")
    first_test(13)

    print("\n")
    second_test(13)

    print("\n")
    second_test(13, 0, 1)

    print("\n")
    first_test(13,0,1)

if __name__ == "__main__":
    main()