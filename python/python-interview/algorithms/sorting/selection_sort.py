
def selection_sort(nums):
    for i in range(len(nums)-1):
        minimum = nums[i]
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < minimum:
                minimum = nums[j]
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

array = [5,9,3,10,45,2,0]
print(selection_sort(array))