
# Sequential Search
def binary_search(arr, item):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        mid = int((first+last)/2)
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

# Recursive version
def rec_bin_search(arr,item):
    if len(arr) == 0:
        return False
    else:
        mid = int(len(arr)/2)
        if arr[mid] == item:
            return True
        else:
            if item < arr[mid]:
                return rec_bin_search(arr[:mid], item)
            else:
                return rec_bin_search(arr[mid+1:], item)


arr = sorted([1,2,3,4,5,6,7,8,9,10])
print(binary_search(arr,4))
print(rec_bin_search(arr,4))

# Sequential Search (Unordered list)
def seq_search(arr, item):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
        else:
            pos += 1
    return found

def ordered_seq_search(arr, item):
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == item:
            return True
        else:
            if arr[pos] > item:
                stopped = True
            else:
                pos += 1
    return found

arr = [1,9,2,8,3,4,7,5,6]
print(seq_search(arr,1))
sorted(arr)
print(ordered_seq_search(arr,1))
    