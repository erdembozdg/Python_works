# Finding Duplicate Values in a list in Python

def duplicate1(arr):
    my_dict = {}
    li = []
    for i in arr:
        if i in my_dict:
            li.append(i)
        else:
            my_dict[i] = 1
    return li

def duplicate2(arr):
    li = []
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            li.append(arr[i])
    return li
arr=[7,5,2,3,0,2,1]
assert duplicate1(arr) == duplicate2(arr)
        