
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def peek(self):
        return self.first.data
    
    def enqueue(self, data):
        node = Node(data)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
            self.length += 1
        return
    
    def dequeue(self):
        if self.first == None:
            print("Queue Empty")
            return None
        elif self.first == self.last:
            self.first = None
        else:
            self.first = self.first.next
            self.length -= 1
            
    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
        else:
            current = self.first
            while current!=None:
                print(current.data, end=" ")
                current = current.next
        print()
        
queue = Queue()
queue.enqueue("This")
queue.enqueue("is")
queue.enqueue("a")
queue.enqueue("Queue")
queue.print_queue()
print(queue.peek())
queue.dequeue()
queue.print_queue()        