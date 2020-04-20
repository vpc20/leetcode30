# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#

# [1, 2, 4, 5, 6, 7, 0]
# [7, 0, 1, 2, 4, 5, 6]


def search(nums, target):
    if not nums:
        return -1

    def binary_search(lo, hi):
        mid = (lo + hi) // 2
        while lo <= mid <= hi:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
            mid = (lo + hi) // 2
        return -1

    def find_max(lo, hi):
        mid = (lo + hi) // 2
        while True:
            if nums[mid] == nums[-1]:
                return len(nums) - 1
            if nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[-1] < nums[0]:
                hi = mid - 1
            else:
                lo = mid + 1
            mid = (lo + hi) // 2

    max_pos = find_max(0, len(nums) - 1)
    left = binary_search(0, max_pos)
    if left != -1:
        return left
    else:
        return binary_search(max_pos + 1, len(nums) - 1)


# def searchx(nums, target):
#     l, r = 0, len(nums) - 1
#
#     while l <= r:
#         m = (l + r) // 2
#         if nums[m] == target:
#             return m
#         elif nums[l] <= nums[m]:
#             if nums[l] <= target < nums[m]:
#                 r = m - 1
#             else:
#                 l = m + 1
#         else:
#             if nums[m] < target <= nums[r]:
#                 l = m + 1
#             else:
#                 r = m - 1
#     return -1


# print(search([4, 5, 6, 7, 0, 1, 2], 0))

# print(search([2, 3, 1], 2))
# print(search([2, 3, 1], 3))
# print(search([2, 3, 1], 1))
# print(search([2, 3, 1], 0))
# print(search([2, 3, 1], 4))

# print(search([1, 2, 3], 1))
# print(search([1, 2, 3], 2))
# print(search([1, 2, 3], 3))

print(search([4, 5, 6, 7, 0, 1, 2], 4))
print(search([4, 5, 6, 7, 0, 1, 2], 5))
print(search([4, 5, 6, 7, 0, 1, 2], 6))
print(search([4, 5, 6, 7, 0, 1, 2], 7))
print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 1))
print(search([4, 5, 6, 7, 0, 1, 2], 2))
print(search([4, 5, 6, 7, 0, 1, 2], 10))

# print(search([3, 4, 5, 6, 1, 2], 2))
