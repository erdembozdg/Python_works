
def merge_sorted_array(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1+arr2
    my_li = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            my_li.append(arr1[i])
            i += 1      
        elif arr1[i] > arr2[j]:
            my_li.append(arr2[j])
            j += 1
    return my_li+arr1[i:]+arr2[j:]

a=[1,3,4,6,20]
b=[2,3,4,5,6,9,11,76] 
print(merge_sorted_array(a,b))