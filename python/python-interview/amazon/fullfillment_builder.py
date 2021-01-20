
def fullfill_builder(nums):
    def helper(nums):
        if len(nums) == 1:
            return 0
        ret = nums[0] + nums[1]
        nums.append(ret)
        return ret
        
    sum = 0
    while True:
        nums.sort()
        sum += helper(nums)  
        if len(nums) > 1:
            nums = nums[2:]
        else:
            break
    return sum

parts = [8, 4, 6, 12]
print(fullfill_builder(parts))
