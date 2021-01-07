class Node:
    def __init__(self, item, left=None, right=None):
        """(Node, object, Node, Node) -> NoneType
        Initialize this node to store item and have children left and right.
        """
        self.item = item
        self.left = left
        self.right = right

    def depth(self):
        current_depth = 0
        if self.left:
            current_depth = max(current_depth, self.left.depth())
        if self.right:
            current_depth = max(current_depth, self.right.depth())
        return current_depth + 1

a = Node(1, Node(2), Node(3))
print(a.depth())