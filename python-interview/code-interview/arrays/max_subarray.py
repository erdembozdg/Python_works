# The Kadane's algorithm
def maxSubArray(nums) -> int:
        maximum = max_array = nums[0]
        for i in range(1, len(nums)):
            max_array = max(nums[i], max_array+nums[i])
            maximum = max(maximum, max_array)
        return maximum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))