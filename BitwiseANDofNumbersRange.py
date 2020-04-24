# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range,
# inclusive.
#
# Example 1:
#
# Input: [5,7]
# Output: 4
#
# Example 2:
#
# Input: [0,1]
# Output: 0


# def range_bitwise_and(m, n):
#     while m < n:
#         n -= (n & -n)
#     return n


def range_bitwise_and(m, n):
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return n << i

# def range_bitwise_and(m, n):
#     b = 2147483647
#     num = m
#     while num < n + 1:
#         # x = num
#         # ctr_trl_zeros = 0
#         # while (x & 1) == 0:
#         #     x = x >> 1
#         #     ctr_trl_zeros += 1
#         # if ctr_trl_zeros >= 4:
#         #     num += 2 ** ctr_trl_zeros
#         print('num', num)
#         b &= num
#         print('b', b)
#         if b == 0:
#             return 0
#         num += 1
#     return b


print(range_bitwise_and(5, 7))
print(range_bitwise_and(5, 8))
print(range_bitwise_and(600000000, 2147483645))

print(range_bitwise_and(600000000, 600000512))
# print(range_bitwise_and(1024, 2048))

# print(0 & 1)
# print(1 & 2)
# print(2 & 3)
# print(3 & 4)
# print(5 & 6)
# print(7 & 8)
# print(9 & 10)

# for i in range(1, 4096):
#     print(i & 2147483647)

# for i in range(600001, 700000):
#     print(range_bitwise_and(600000, i))


# print(600000000 & 600000511)
# print(600000000 & 600000512)
