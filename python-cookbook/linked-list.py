
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
    def getData(self):
        return self.data
    
    def setData(self, value):
        self.data = value
        
    def getNext(self):
        return self.next
    
    def setNext(self, value):
        self.next = value
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError
        
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def printList(self):
        """Print the list"""
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()
            
ll = LinkedList()
ll.add('l')
ll.add('H')
ll.remove('l')
ll.printList()