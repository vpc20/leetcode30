# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note: Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4


def single_num(arr):
    seen = set()
    for e in arr:
        if e in seen:
            seen.remove(e)
        else:
            seen.add(e)
    return next(iter(seen))


# def single_num(arr):
#     sum = 0
#     for e in arr:
#         sum ^= e
#     return sum


arr1 = [2, 2, 1, 3, 3]
print(single_num(arr1))
