#  Given an integer array, output all the unique sum

def arr_sum1(arr, sum):
    i, j = 0, len(arr) -1
    arr.sort()
    li = []
    while i < j:
        if arr[i] + arr[j] > sum:
            j -= 1
        elif arr[i] + arr[j] < sum:
            i += 1
        else:
            li.append((arr[i], arr[j]))
            i += 1
    return li

def arr_sum2(arr, sum):
    li = []
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                li.append((arr[i], arr[j]))
    return li

assert arr_sum1([2,4,6],10) == arr_sum2([2,4,6],10)            
    
    