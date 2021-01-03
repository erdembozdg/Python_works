
# Array Pair Sum
def pair_sum(arr, k):
    pairs = []
    for i in arr:
        if (k - i) in arr:
            pairs.append((i, k-i))
            arr.pop(i)
    return pairs
print(pair_sum([1,3,2,2],4))

# Find missing elements
def finder(arr1, arr2):
    for i in arr1:
        if i in arr2:
            arr2.remove(i)
    return arr2
arr1 = [1,2,3,4,6,7]
arr2 = [3,7,2,1,4,6,5]
print(finder(arr1,arr2))

# Largest Continuous Sum
def large_cont_sum(arr):
    current_sum = max_sum = arr[0]
    for i in arr[1:]:
        current_sum = max(current_sum+i, i)
        max_sum = max(current_sum, max_sum)
    return max_sum
print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

def rotLeft(a, d):
    return a[d:] + a[:d]
print(rotLeft([1,2,3,4],1))

import math
def minimumAbsoluteDifference(arr):
    least = max(max(arr), min(arr) * -1) * 2
    arr = sorted(arr)
    for i in range(0, math.ceil(len(arr) / 2)):
        f = abs(arr[i] - arr[i + 1])
        b = abs(arr[-(i + 1)] - arr[-(i + 2)])
        if (least > min(f, b)):
            least = min(f, b)
            if (least == 0):
                return 0
    return least 


