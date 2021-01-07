#Look-up : O(n)
#Insert : O(n)
#Delete : O(n)
#Append : O(1)
#Prepend : O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
        
    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
            
    def prepend(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
            self.length = 1
        else:
            node.next = self.head
            self.head = node
            self.length += 1
            
    def insert(self, pos, data):
        node = Node(data)
        if pos >= self.length:
            self.tail.next = node
            self.tail = node
            self.length += 1
        elif pos == 0:
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            current_node = self.head
            for _ in range(pos-1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.length += 1
            
    def delete_by_pos(self, pos):
        if self.head == None:
            print("Empty")
            return
        if pos == 0:
            self.head = self.head.next
            if self.head == None or self.head.next==None:
                self.tail = self.head
            self.length -= 1
            return
        if pos >= self.length:
            pos = self.length - 1
        current_node = self.head
        for _ in range(pos-1):
            current_node = current_node.next
        current_node.next = current_node.next.next 
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return
            
    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end=" ")
                current_node = current_node.next
        print()

def reverse(linked_list):
    if linked_list.length <= 1:
        return linked_list
    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None
        linked_list.head = first
    return linked_list

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(2)
    linked_list.append(9)
    linked_list.print_list() # 5 2 9 
    linked_list.prepend(4)  
    linked_list.print_list() # 4 5 2 9 
    linked_list.insert(2,7)
    linked_list.print_list() #4 5 7 2 9
    linked_list.insert(0,0)
    linked_list.insert(6,0)
    linked_list.insert(9,3)
    linked_list.print_list() #0 4 5 7 2 9 0 3
    linked_list.delete_by_pos(3)
    linked_list.print_list() #0 4 5 2 9 0 3
    reverse(linked_list).print_list()



            
        