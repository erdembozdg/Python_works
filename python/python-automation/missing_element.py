# finding which element is missing from second array

def missing(arr1, arr2):
    arr1.sort()
    arr2.sort()
    my_dict = {}
    
    for i in arr1:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    
    for i in arr2:
        if i in my_dict:
            my_dict[i] -= 1
        else:
            my_dict[i] = 1
    
    li = []    
    for i in my_dict:
        if my_dict[i] == 1:
            li.append(i)
    return li

print(missing([1,2,5,3,4],[1,5,4,2]))
        