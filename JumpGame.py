# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
#
# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
#


# def can_jump_aux(nums):
#     i = 0
#     last_index = len(nums) - 1
#     while True:
#         if i >= last_index:
#             return True
#         if nums[i] == 0:
#             return False
#         i += nums[i]


# dynamic programming solution, O(n^2) time complexity
def can_jump_dyna(nums):
    dp = [True] + [False] * (len(nums) - 1)
    for i in range(1, len(nums)):
        for j in range(i):
            if dp[j] and j + nums[j] >= i:
                dp[i] = True
                break
        else:
            dp[i] = False
    return dp[-1]


# dynamic programming solution, O(n^2) time complexity
def can_jump_dyna1(nums):
    dp = [True] + [False] * (len(nums) - 1)
    for i in range(len(nums)):
        if dp[i]:
            for j in range(i, i + nums[i] + 1):
                if j < len(nums):
                    dp[j] = True
    return dp[-1]


# greedy solution, O(n) time complexity
def can_jump(nums):
    lasti = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= lasti:
            lasti = i
    return lasti == 0


# def can_jump(nums):
#     len1 = len(nums)
#     nexti = 0
#     for i in range(len1):
#         if i + nums[i] >= len1 - 1:
#             return True
#         nexti = i + nums[i]
#     return False


# def canJump(nums):
#     n = len(nums)
#     if n <= 1:
#         return True
#
#     dp = [True] + [False] * (n - 1)
#     for i in range(1, n):
#         dp[i] = any(nums[j] >= (i - j) for j in range(i) if dp[j])
#     return dp[n - 1]


# arr = [2, 3, 1, 1, 4]
# print(can_jump_dyna(arr))
# print(canJump(arr))
#
# arr = [3, 2, 1, 0, 4]
# print(can_jump_dyna(arr))
# print(canJump(arr))
#
# arr = [2, 0]
# print(can_jump_dyna(arr))
# print(canJump(arr))
#
# arr = [2, 5, 0, 0]
# print(can_jump_dyna(arr))
# print(canJump(arr))
#
# arr = [1, 1, 2, 2, 0, 1, 1]
# print(can_jump_dyna(arr))
# print(canJump(arr))

print('-----')
arr = [2, 3, 1, 1, 4]
# arr = [0, 2]
# arr = [2, 0]
# arr = [2, 5, 0, 0]
print(can_jump_dyna1(arr))
