#Push (Insert) - O(1)
#Pop (Remove) - O(1)
#Peek (Retrieve the top element) - O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def peek(self):
        if self.top == None:
            return None
        return self.top.data
    
    def push(self, data):
        node = Node(data)
        if self.top == None:
            self.top = node
            self.bottom = node
        else:
            node.next = self.top
            self.top = node
        self.length += 1
        
    def pop(self):
        if self.top == None:
            print("Empty")
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None
    
    def print_stack(self):
        if self.top == None:
            print("Stack Empty")
        else:
            current = self.top
            while(current != None):
                print(current.data, end=" ")
                current = current.next
        print()


stack = Stack()
stack.push("Andrei")
stack.push("Courses")
stack.push("Are")
stack.push("Awesome")
stack.print_stack()
stack.pop()
stack.print_stack()
print(stack.peek())



