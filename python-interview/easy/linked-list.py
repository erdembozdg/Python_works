
class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def nth_to_last_node(n, head):
    slow, fast = head, head
    while n > 0 and fast:
        fast=fast.nextnode
        n-=1
    if not fast:
        return head
    while fast:
        fast=fast.nextnode
        slow=slow.nextnode
    return slow
    pass

def reverse(head):
    cur = head
    pre, nxt = None, None
    while cur:# watch out
        nxt = cur.nextnode
        cur.nextnode = pre
        pre = cur
        cur = nxt
    return pre #watch out
    pass

def cycle_check(node):
    #     Use fast and slow pointer
    fast, slow = node, node
    while fast and fast.nextnode:
        fast = fast.nextnode
        if fast == slow:
            return True
        fast = fast.nextnode
        slow = slow.nextnode
    return False
    pass #Your function should return a boolean

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = nth_to_last_node(2, a)

