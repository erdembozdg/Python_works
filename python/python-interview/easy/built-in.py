from functools import reduce

lst =[47,11,42,13]
print(list(map(lambda x,y: x*y, lst, lst)))
print(reduce(lambda x,y: x if x > y else y, lst))
print(list(filter(lambda x: x % 2 == 0, lst)))
print(list(zip(lst, lst)))
print(list(enumerate(lst, start=3)))