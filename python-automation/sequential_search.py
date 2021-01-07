# Sequential search for Ordered and Unordered list

def ordered_search(arr, item):
    pos = 0
    found = False
    stopped = False
    
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == item:
            found = True
        else:
            if arr[pos] > item:
                stopped = True
            else:
                pos += 1
    return found

def unordered_search(arr, item):
    pos = 0
    found = False
    
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
        else:
            pos += 1
    return found

