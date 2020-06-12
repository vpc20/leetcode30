import sys


def max_sum(arr, k):
    curr_sum = sum(arr[:k])  # sliding window of length k
    max_sum = curr_sum
    l = 1
    r = k

    while r < len(arr):
        curr_sum = curr_sum - arr[l - 1] + arr[r]
        max_sum = max(max_sum, curr_sum)
        l += 1
        r += 1
    return max_sum


print(max_sum([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))
