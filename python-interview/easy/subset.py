# Maximum sum of a subarray of sie K
def max_sum_subarray(arr, k):
    max_sum, window_sum = 0, 0
    start = 0
    for end in range(len(arr)):
        window_sum += arr[end]
        if end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))

  
    


























