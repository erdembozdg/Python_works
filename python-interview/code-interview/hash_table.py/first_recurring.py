# The time complexity is O(n)
def first_rec(nums):
    my_dict = {}
    for i in nums:
        if i in my_dict:
            return i
        else:
            my_dict[i] = i
    return None

print(first_rec([2,1,4,1,5,2,6]))