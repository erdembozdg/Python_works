
class Deque:
    def __init__(self):
        self.items = []
    def is_emplty(self):
        return self.items == []
    def add_front(self, item):
        self.items.insert(0, item)
    def remove_front(self, item):
        return self.items.pop(0)
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[self.size() - 1]
    
class Queue2Stacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, item):
        self.in_stack.append(item)
        
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()   