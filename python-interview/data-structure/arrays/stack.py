
class Stack:
    def __init__(self):
        self.array = []
        
    def peek(self):
        return self.array[len(self.array) - 1]
        
    def push(self, data):
        self.array.append(data)
        return
    
    def pop(self):
        if len(self.array) != 0:
            self.array.pop()
            return
        else:
            print("Empty")
            return
    
    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i], end=" ")
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



