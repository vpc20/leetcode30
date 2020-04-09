# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


# dynamic simplified
import sys


def max_subarr_sum(arr):
    """ Maximum sub-array function computes for the largest sum of sub-array

    :params arr: input array
    :return: maximum sum of sub-array
    """
    if not arr:
        return 0
    subarr_sum = 0
    maxsum = -sys.maxsize
    for num in arr:
        subarr_sum = max(subarr_sum + num, num)
        maxsum = max(maxsum, subarr_sum)
    return maxsum


def max_subarr_sum_brute(arr):
    return max([sum(arr[i:j + 1]) for i in range(len(arr) - 1) for j in range(i + 1, len(arr))])


print(max_subarr_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarr_sum_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(max_subarr_sum([-2, 1, -3, 4]))
