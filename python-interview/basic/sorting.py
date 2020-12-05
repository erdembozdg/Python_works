
def getKey(s):
    if s.islower():
        return (1, s)
    elif s.isupper():
        return (2, s)
    elif s.isdigit():
        if int(s)%2 == 1:
            return (3, s)  
        else:
            return (4, s)
    
print(*sorted("Sorting1234", key=getKey), sep='')

# Bubble Sort
def countSwaps(a):
    numSwaps = 0
    while True:
        swapFlag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                numSwaps += 1
                swapFlag = True
                         
        if not swapFlag:
            break
    print('Array is sorted in', numSwaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])
countSwaps([3, 1, 2, 4])