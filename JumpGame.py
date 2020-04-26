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

def can_jump_aux(nums, i):
    last_index = len(nums) - 1
    for k in range(i, i + nums[0]):
        while True:
            if k >= last_index:
                return True
            if nums[k] == 0:
                return False
            can_jump_aux(nums, k + nums[k])


def can_jump(nums):
    # x = nums[0]
    # for i in range(x + 1):
    #     if can_jump_aux(nums[i:], 0):
    #         return True
    # return False
    return can_jump_aux(nums, 0)


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


def canJump(nums):
    n = len(nums)
    if n <= 1:
        return True

    dp = [True] + [False] * (n - 1)
    for i in range(1, n):
        dp[i] = any(nums[j] >= (i - j) for j in range(i) if dp[j])
    return dp[n - 1]


arr = [2, 3, 1, 1, 4]
print(can_jump_dyna(arr))
print(canJump(arr))

arr = [3, 2, 1, 0, 4]
print(can_jump_dyna(arr))
print(canJump(arr))

arr = [2, 0]
print(can_jump_dyna(arr))
print(canJump(arr))

arr = [2, 5, 0, 0]
print(can_jump_dyna(arr))
print(canJump(arr))

arr = [1, 1, 2, 2, 0, 1, 1]
print(can_jump_dyna(arr))
print(canJump(arr))

print('-----')
arr = [1, 1, 1, 1]
print(can_jump_dyna(arr))
