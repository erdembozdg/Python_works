
import heapq

li = [5, 7, 9, 1, 3]

heapq.heapify(li)
print(list(li))

heapq.heappush(li, 4)
print(list(li))

print(heapq.heappop(li))
print(heapq.heappushpop(li, 2))
