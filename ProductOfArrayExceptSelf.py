# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the
# whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose
# of space complexity analysis.)


def product_except_self_naive(nums):
    output = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if j != i:
                prod *= nums[j]
        output.append(prod)
    return output


# def productExceptSelf(nums):
#     output = [0] * len(nums)
#     if nums.count(0) > 1:
#         return output
#     if nums.count(0) == 1:
#         prod = 1
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 zero_idx = i
#             else:
#                 prod *= nums[i]
#         output[zero_idx] = prod
#         return output
#
#     pref = [nums[0]]  # prefix product
#     for i in range(1, len(nums)):
#         pref.append(nums[i] * pref[-1])
#     # pref = nums.copy()  # prefix product
#     # for i in range(1, len(pref)):
#     #     pref[i] *= pref[i - 1]
#     return [int(pref[-1] / nums[i]) for i in range(len(nums))]


# def productExceptSelf(nums):
#     pref = nums.copy()  # prefix product
#     for i in range(1, len(pref)):
#         pref[i] *= pref[i - 1]
#
#     suff = nums.copy()  # suffix product
#     for i in range(-2, -len(suff) - 1, -1):
#         suff[i] *= suff[i + 1]
#
#     result = []
#     for i in range(len(nums)):
#         if i == 0:
#             result.append(suff[i + 1])
#         elif i == len(nums) - 1:
#             result.append(pref[i - 1])
#         else:
#             result.append(pref[i - 1] * suff[i + 1])
#     return result


# def productExceptSelf(nums):
#     pref = nums.copy()  # prefix product
#     suff = nums.copy()  # suffix product
#     for i in range(1, len(pref)):
#         pref[i] *= pref[i - 1]
#         suff[-i - 1] *= suff[-i]
#
#     result = []
#     for i in range(len(nums)):
#         if i == 0:
#             result.append(suff[i + 1])
#         elif i == len(nums) - 1:
#             result.append(pref[i - 1])
#         else:
#             result.append(pref[i - 1] * suff[i + 1])
#     return result


def product_except_self(nums):
    pref = [1] * len(nums)  # prefix product
    suff = [1] * len(nums)  # suffix product

    for i in range(1, len(nums)):
        pref[i] = nums[i - 1] * pref[i - 1]
        suff[-i - 1] = nums[-i] * suff[-i]

    return [pref[i] * suff[i] for i in range(len(nums))]


# nums = [1, 2, 3, 4]
# nums = [1, 0, 2, 3]
# nums = [1, 0, 2, 0]
# nums = [1, 0]
# nums = [1, 1]
# nums = [9, 0, -2]
nums = [1, 2, 3, 4, 5]
print('input', nums)
print('correct', product_except_self_naive(nums))
print(product_except_self(nums))

#   1     2     3     4     5

#  120   60    40    30    24

#   1     2     6    24   120   --- pref

#  120   120   60    20     5   --- suff


#  0    1    2    3    4
# -5   -4   -3   -2   -1
