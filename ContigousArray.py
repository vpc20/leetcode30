# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
# Note: The length of the given binary array will not exceed 50,000.


def find_max_len_brute(nums):
    maxlen = 0
    for i in range(len(nums) - 1):
        for j in range(i + 2, len(nums) + 1):
            sub_arr = nums[i:j]
            if sub_arr.count(0) == sub_arr.count(1):
                maxlen = max(maxlen, len(sub_arr))
    return maxlen


# public class Solution {
#
#     public int findMaxLength(int[] nums) {
#         Map<Integer, Integer> map = new HashMap<>();
#         map.put(0, -1);
#         int maxlen = 0, count = 0;
#         for (int i = 0; i < nums.length; i++) {
#             count = count + (nums[i] == 1 ? 1 : -1);
#             if (map.containsKey(count)) {
#                 maxlen = Math.max(maxlen, i - map.get(count));
#             } else {
#                 map.put(count, i);
#             }
#         }
#         return maxlen;
#     }
# }

# def find_max_len(nums):
#     pos = 0
#     ypos_arr = [0]
#     for i in range(len(nums)):
#         pos += (1 if nums[i] == 1 else -1)
#         ypos_arr.append(pos)
#
#     d = {}
#     maxlen = 0
#     for i, num in enumerate(ypos_arr):
#         if num in d:
#             maxlen = max(maxlen, i - d[num])
#         else:
#             d[num] = i
#     return maxlen

# this is the compact version of code above
# def find_max_len(nums):
#     hashmap = {0: -1}
#     maxlen = 0
#     count = 0
#     for i in range(len(nums)):
#         count += (1 if nums[i] == 1 else -1)
#         if count in hashmap:
#             maxlen = max(maxlen, i - hashmap[count])
#         else:
#             hashmap[count] = i
#     return maxlen

# this is the another compact version of code above
def find_max_len(nums):
    pos = maxlen = 0
    d = {0: 0}
    for i, num in enumerate(nums):
        pos += (1 if num == 1 else -1)
        if pos in d:
            maxlen = max(maxlen, i + 1 - d[pos])
        else:
            d[pos] = i + 1
    return maxlen


# nums = [1, 1, 1, 0, 1, 0, 1, 1]
# nums = [1, 0, 1, 1, 1, 0, 1, 1]
# nums = [1, 1, 1, 0, 1, 1, 0, 1, 1]
# nums = [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
# nums = [1, 1, 1, 1, 1, 1, 1, 1, 0]
# nums = [0, 1, 1, 1, 1, 1, 1, 1, 1]
# nums = [1, 0, 1, 0]
# nums = [1, 1, 1, 1]
# nums = [0, 0, 1, 0, 0, 0, 1, 1]


nums = [1, 0, 0, 1, 0]

print(find_max_len_brute(nums))
print(find_max_len(nums))
