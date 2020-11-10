import os
import datetime

def list_directories(path):
    for file in os.listdir(path):
        full_path = os.path.join(path, file);
        if(os.path.isdir(full_path)):
            list_directories(full_path)
        else:
            print(full_path)

list_directories(os.getcwd())

class A:
    def go(self):
        print("go A go")
    def stop(self):
        print("stop A stop")
    def pause(self):
        raise Exception("Not implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go")
    def stop(self):
        super(B, self).stop()
        print("stop B stop")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go")
    def stop(self):
        super(C, self).stop()
        print("stop C stop")

class D(B, C):
    def go(self):
        super(D, self).go()
        print("go D go")
    def stop(self):
        super(D, self).stop()
        print("stop D stop")

d = D()
d.go()
d.stop()

class Node:
    def __init__(self, name):
        self._children = []
        self.name = name

    def __repr__(self):
        return "<Node '{}'>".format(self.name)

    def append(self, *args, **kwargs):
        self._children.append(*args, **kwargs)

    def print_all(self):
        print(self)
        for node in self._children:
            node.print_all()

oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oRoot.append(oChild1)
oChild1.append(oChild2)
oRoot.print_all()


        
