def moveZeroes(nums) -> None:
    z = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[z] = nums[z], nums[i]
            z += 1
    return nums
print(moveZeroes([0,1,0,3,12]))