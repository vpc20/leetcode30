# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number
# equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example:
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 02 = 1


def is_happy(n):
    if n == 1:
        return True
    seen = set()
    while n != 1:
        sum = 0
        for digit in str(n):
            sum += pow(int(digit), 2)
        n = sum
        if n in seen:
            return False
        else:
            seen.add(n)
    return True


def is_happy1(n):
    if n == 1:
        return True
    seen = set()
    while n != 1:
        n = sum([pow(int(digit), 2) for digit in str(n)])
        if n in seen:
            return False
        else:
            seen.add(n)
    return True


def is_happy2(n):
    for i in range(19):
        n = sum([pow(int(digit), 2) for digit in str(n)])
        if n == 1:
            return True
    return False


def is_happy3(n):
    ctr = 0
    if n == 1:
        return True, ctr
    seen = set()
    while n != 1:
        sum = 0
        for digit in str(n):
            sum += pow(int(digit), 2)
        n = sum
        ctr += 1
        if n in seen:
            return False, ctr
        else:
            seen.add(n)
    return True, ctr


# this can be used to compute sum instead of the for loop above
def sum_of_squares(n):
    sum = 0
    q = 1
    while q:
        q, n = divmod(n, 10)
        sum += q * q
    sum += n * n
    return sum


def sum_of_squares1(n):
    return sum([pow(int(digit), 2) for digit in str(n)])


# print(is_happy(1))
print(is_happy(19))
print(is_happy(20))

print(is_happy1(19))
print(is_happy1(20))

print(is_happy2(19))
print(is_happy2(20))

# print(sum_of_squares(19))
# print(sum_of_squares1(19))

max_ctr = 0
for i in range(810):
    print(i)
    x, ctr = is_happy3(i)
    max_ctr = max(max_ctr, ctr)
print(max_ctr)
