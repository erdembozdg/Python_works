# find the largest continious sum

def continious_sum(arr):
    if len(arr) == 0:
        return 0
    
    current_sum = 0
    max_sum = 0
    
    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(continious_sum(arr))