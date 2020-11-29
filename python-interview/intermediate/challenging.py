# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    code = [0,0,7]
    for i in nums:
        if len(code) > 0 and i == code[0]:
            code.pop(0)
    return len(code) == 0
print(spy_game([1,2,4,0,0,7,5]))


def print_big(letter):
    pattern = {1:'  *  ', 2: ' * * ', 3: '*****', 4: '*   *'}
    alphabet = {'A': [1,2,3,4,4]}
    for i in alphabet[letter.upper()]:
        print(pattern[i])
print_big('A')
 
# Largest Continuous Sum
def large_cont_sum(arr):
    max_sum = current_sum = arr[0]
    for n in arr[1:]:
        current_sum = max(current_sum+n, n)
        max_sum = max(current_sum, max_sum)      
    return max_sum
print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

def uni_char(s):
    s1 = set()
    for i in list(s):
        if i in s1:
            return False
        else:
            s1.add(i)
    return True
print(uni_char('abcde'))

