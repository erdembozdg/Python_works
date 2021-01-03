
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

def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr
arr = [3,2,13,4,6,5,7,8,1,20]
print(bubble_sort(arr))

def selection_sort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if arr[location]>arr[positionOfMax]:
                positionOfMax = location
        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp

def insertion_sort(arr): 
    for i in range(1,len(arr)): 
        currentvalue = arr[i]
        position = i
        while position>0 and arr[position-1]>currentvalue:    
            arr[position]=arr[position-1]
            position = position-1
        arr[position]=currentvalue
        
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        print(r"{self.name} {self.score}")
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.name > b.name:
            return 1
        return -1
        