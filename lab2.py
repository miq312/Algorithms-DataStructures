#skonczone
class Element:
      def __init__(self, data):
           self.data = data
           self.next = None
      def __str__(self):
        return str(self.data)
      
class LinkedList:
    def __init__(self):
            self.head = None

    def destroy(self):
          self.head = None

    def add(self, other: Element):
        if self.head == None:
            self.head = other
        else:
            other.next = self.head
            self.head = other
    
    def append(self, app: Element):
        #app = Element(other)
        if self.head == None:
            self.head = app
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = app

    def remove(self):
          if self.is_empty():
               self.destroy()
               print("REMOVE::Lista jest pusta")
          else:
               self.head = self.head.next
          
    def remove_end(self):
        if self.head != None and self.length() > 1:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
        else:
            self.head = None
    
    def is_empty(self) -> bool:
          if self.head == None:
            return True
          else:
            return False
    
    def length(self) -> int:
        length = 0
        current = self.head
        while current != None:
            length += 1
            current = current.next
        return length

    def get(self):
          return self.head.data
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current))
            current = current.next
        return '\n'.join(elements)
    
def main():
    uni_data = [('AGH', 'Kraków', 1919),
               ('UJ', 'Kraków', 1364),
               ('PW', 'Warszawa', 1915),
               ('UW', 'Warszawa', 1915),
               ('UP', 'Poznań', 1919),
               ('PG', 'Gdańsk', 1945)]
    u0 = Element(uni_data[0])
    u1 = Element(uni_data[1])
    u2 = Element(uni_data[2])
    u3 = Element(uni_data[3])
    u4 = Element(uni_data[4])
    u5 = Element(uni_data[5])

    uczelnie = LinkedList()

    uczelnie.append(u0)
    uczelnie.append(u1)
    uczelnie.append(u2)
    uczelnie.add(u3)
    uczelnie.add(u4)
    uczelnie.add(u5)

    print(uczelnie)
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get(), "\n")
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy() 
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(u0)
    uczelnie.remove_end()
    print(uczelnie.is_empty()) 
  
if __name__ == "__main__":
    main()
    