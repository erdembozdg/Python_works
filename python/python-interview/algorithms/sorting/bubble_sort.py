
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

array = [5,9,3,10,45,2,0]
print(bubble_sort(array))
           