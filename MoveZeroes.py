# Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# def move_zeroes(nums):
#     i = 0
#     j = len(nums) - 1
#     while i < j:
#         if nums[i] == 0:
#             for k in range(i, j):
#                 nums[k] = nums[k + 1]
#             nums[j] = 0
#             j -= 1
#         else:
#             i += 1

# def move_zeroes(nums):
#     arr = [0] * len(nums)
#     i = 0
#     for num in nums:
#         if num != 0:
#             arr[i] = num
#             i += 1
#     for i in range(len(nums)):
#         nums[i] = arr[i]


# def move_zeroes(nums):
#     arr = [num for num in nums if num != 0]
#     for i in range(len(arr)):
#         nums[i] = arr[i]
#     for i in range(len(arr), len(nums)):
#         nums[i] = 0


def move_zeroes(nums):
    idx = 0
    for num in nums:
        if num != 0:
            nums[idx] = num
            idx += 1
    for i in range(idx, len(nums)):
        nums[i] = 0


nums = [0, 1, 0, 3, 12]
# nums = [0, 0, 1]
move_zeroes(nums)
print(nums)
