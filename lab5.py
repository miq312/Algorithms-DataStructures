class Node:
    def __init__(self, key, value, right, left):
        self.key = key
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return f"{self.key}:{self.value}"
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def search(self, key):
        current = self.root
        
        return self.rsearch(key, current)

    def rsearch(self, key, current):
        if current == None:
            return None

        if current.key == key:
            return current.value
        
        if key > current.key:
            return self.rsearch(key, current.right)
        
        return self.rsearch(key, current.left)
    
    def insert(self, node: Node):
        if self.root == None:
            self.root = node
            return
        return self.rinsert(node, self.root)
    
    def rinsert(self, newNode, parentNode):
        if parentNode.key == newNode.key:
            parentNode.value = newNode.value
        if newNode.key < parentNode.key:
            if parentNode.left == None:
                parentNode.left = newNode
            else:
                return self.rinsert(newNode, parentNode.left)
        if newNode.key > parentNode.key:
            if parentNode.right == None:
                parentNode.right = newNode
            else:
                return self.rinsert(newNode, parentNode.right)
    
    def delete(self, key):
        current = self.root
        return self.rdelete(current, key)
    
    def rdelete(self, current, key):
        if current.left == None and current.right == None:
            

def main():
    t = BinaryTree()

if __name__ == "__main__":
    main()