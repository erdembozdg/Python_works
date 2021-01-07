
class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def peek(self):
        if len(self.s1) == 0:
            print("Queue empty")
        else:
            return self.s1[len(self.s1)-1]
        
    def enqueue(self, data):
        for i in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)
        self.s1.append(data)
        for i in range(len(self.s2)):
            item = self.s2.pop()
            self.s1.append(item)
        return

    def dequeue(self):
        if len(self.s1)==0:
            print("Queue Empty")
            return
        else:
            return self.s1.pop()

    def print_queue(self):
        if len(self.s1) == 0:
            print("Queue Empty")
            return
        for i in range(len(self.s1) - 1,0,-1):
            print(f'{self.s1[i]} <<-- ',end='')
        print(self.s1[0])
        return
    
queue = Queue()
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(0)
queue.print_queue()
#2 <<-- 5 <<-- 0
queue.dequeue()
queue.print_queue()
#5 <<-- 0
print(queue.peek())
#5
queue.dequeue()
queue.print_queue()
