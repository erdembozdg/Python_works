
def bubble_sort(nums):
    for n in range(len(nums) - 1, 0, -1):
        for i in range(n):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

array = [5,9,3,10,45,2,0]
print(bubble_sort(array))
           