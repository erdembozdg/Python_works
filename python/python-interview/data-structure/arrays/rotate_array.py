# O(n*k)
def brute_force_roration(nums, k):
    for _ in range(k):
        temp = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp
    return nums

# O(n)
def better_roration(nums, k):
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
    nums = reverse(nums,0,len(nums)-1)
    nums = reverse(nums,0,k%len(nums)-1)
    nums = reverse(nums,k%len(nums),len(nums)-1)
    return nums
print(brute_force_roration([1,2,3,4,5,6,7,8,9], 3)) 
print(better_roration([1,2,3,4,5,6,7,8,9], 3))
        
        