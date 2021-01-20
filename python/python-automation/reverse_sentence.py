
def reverse1(s):
    arr = s.split(" ")
    num = len(arr) - 1
    li = []
    while num >= 0:
        li.append(arr[num])
        num -= 1
    return " ".join(li)

def reverse2(s):
    return " ".join(reversed(s.split(" ")))

my_str="Welcome to Python"
assert reverse1(my_str) == reverse2(my_str)
