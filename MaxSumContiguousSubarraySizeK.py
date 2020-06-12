import sys

from RandomData import random_int_array


def max_sum_naive(arr, k):
    if k > len(arr):
        return None
    maxsum = -sys.maxsize
    for i in range(len(arr) - k + 1):
        maxsum = max(maxsum, sum(arr[i:i + k]))
    return maxsum


# n = 10   k = 3
# 0 1 2 3 4 5 6 7 8 9


def max_sum(arr, k):
    if k > len(arr):
        return None
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


assert max_sum_naive([1, 2, 3], 3) == 6
assert max_sum([1, 2, 3], 3) == 6

assert max_sum_naive([1, 2, 3, 4], 3) == 9
assert max_sum([1, 2, 3, 4], 3) == 9

assert max_sum_naive([4, 3, 2, 1], 3) == 9
assert max_sum([4, 3, 2, 1], 3) == 9

assert max_sum_naive([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3) == 16
assert max_sum([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3) == 16

for _ in range(10000):
    arr = random_int_array(20, 15)
    print(arr)
    for k in range(1, 6):
        assert max_sum_naive(arr, k) == max_sum(arr, k)
