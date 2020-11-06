
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def x(*a, **b):
    print(a, b)

x(numbers, a='erdem')