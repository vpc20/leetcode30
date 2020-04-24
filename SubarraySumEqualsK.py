# Given an array of integers and an integer k, you need to find the total number of continuous subarrays
# whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
#
# Note:
#     The length of the array is in range [1, 20,000].
#     The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
from collections import defaultdict


def subarray_sum_brute(nums, k):
    ctr = 0
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if sum(nums[i:j + 1]) == k:
                ctr += 1
    return ctr


def subarray_sum(nums, k):
    pref_sums = [nums[0]]
    desired_val = {nums[0]}  # this is a set
    ctr = 0
    for i in range(1, len(nums)):
        if k - nums[i] in desired_val:
            ctr += 1
        pref_sums.append(nums[i] + pref_sums[i - 1])
    print(pref_sums)
    print(desired_val)
    return ctr


# [1, 2, 3, 4, 5, 6, 7] 9
# [1, 3, 6, 10, 15, 21, 28] prefix sum

# print(subarray_sum_brute([1, 1, 1, ], 2))
# print(subarray_sum_brute([1, 2, 3, 4, 5, 6, 7], 9))
# print(subarray_sum_brute([-1, 3, 3, 4, 5, 6, 7], 9))

print(subarray_sum([1, 2, 3, 4, 5, 6, 7], 9))

# nums = [-1, 3, 3, 4, 5, 6, 7]
# for i in range(1, len(nums)):
#     nums[i] += nums[i-1]
# print(nums)
