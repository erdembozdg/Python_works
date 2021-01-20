

def factorial1(num):
    f = 1
    for i in range(1, num+1):
        f = i * f
    return f

def factorial2(num):
    if num <= 1:
        return 1
    return num*factorial2(num-1)

print(factorial1(5))
print(factorial2(5))
        