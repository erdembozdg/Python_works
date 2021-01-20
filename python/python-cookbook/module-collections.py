from collections import Counter, defaultdict, namedtuple
from collections import deque
c = Counter("Hello World")
print(Counter(("Hello World").split(" ")))
f = defaultdict(int)
f['x'] += 2
f['y']
print(f)

s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]
d = defaultdict(list)
for k,v in s:
   d[k] = v
print(d) 

P1 = namedtuple('P1', 'x y z')
P2 = namedtuple('P2', ['x', 'y', 'z'])
P3 = namedtuple('P3', 'x, y, z')
p1 = P1('a', 'b', 'c')
p2 = P2('a', 'b', 'c')
p3 = P3('a', 'b', 'c')
print(p1.x, p2.x, p3.x, p1.y, p2.z, p3.z)

e = deque('Erdem')
e.pop()
e.popleft()
e.appendleft('s')
print(list(e))
e.rotate(-1)
print(list(e))
print(list(reversed(e)))

#Breadth First Search
def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
    # The oldest seen (but not yet visited) node will be the left most one.
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                # When we see a new node, we add it to the right side of the queue.
                q.append(neighbor)
    return distances
graph = {1:[2,3], 2:[4], 3:[4,5], 4:[3,5], 5:[]}
print(bfs(graph, 1))
