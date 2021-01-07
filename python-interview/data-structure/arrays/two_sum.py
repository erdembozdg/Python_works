
def twoSum(arr, target):
    my_li = []
    for i in range(len(arr)-1):
        for j in range(1, len(arr)):
            if i < j:
                if arr[i] + arr[j] == target:
                    my_li.append(i)
                    my_li.append(j)
    return my_li

print(twoSum([2,7,11,15], 9))

                