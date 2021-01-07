
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0
        
    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
            self.number_of_nodes = 1
            return
        else:
            current = self.root
            while True:
                if current.data > node.data:
                    if current.left == None:
                        current.left = node
                        return
                    else:
                        current = current.left
                elif current.data < node.data:
                    if current.right == None:
                        current.right = node
                        return
                    else:
                        current = current.right
                self.number_of_nodes += 1
    
    def search(self, data):
        if self.root == None:
            return "Empty"
        else:
            current = self.root
            while True:
                if current == None:
                    return "Not found"
                elif current.data == data:
                    return "Found"
                else:
                    if current.data > data:
                        current = current.left
                    elif current.data < data:
                        current = current.right
                        
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(13)
bst.insert(65)
bst.insert(0)
bst.insert(10)
print(bst.search(10))
            