
class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []
        
    def push(self, data):
        self.main_stack.append(data)
        
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return
        
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])
    
    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()
    
    def get_max_item(self):
        return self.max_stack.pop()

if __name__ == "__main__":
    max_stack = MaxStack()
    max_stack.push(14)
    max_stack.push(4)
    max_stack.push(24)
    print(max_stack.get_max_item())