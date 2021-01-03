# brute force O(n^2)
def find_duplicate1(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
# O(nlogn)
def find_duplicate2(nums):
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False
# O(n)
def find_duplicate3(nums):
    dicty = {}
    for i in range(len(nums)):
        if nums[i] in dicty:
            return True
        else:
            dicty[nums[i]] = True
    return False
        
print(find_duplicate1([1,2,46,32,98,61,34,46]))
print(find_duplicate2([1,2,46,32,98,61,34,46]))
print(find_duplicate3([1,2,46,32,98,61,34,46]))