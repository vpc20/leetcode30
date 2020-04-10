# Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.
#
# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
# Example 3:
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
# Example 4:
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#
# Note:
#
# 1. 1 <= S.length <= 200
# 2. 1 <= T.length <= 200
# 3. S and T only contain lowercase letters and '#' characters.
#
# Follow up:
#     Can you solve it in O(N) time and O(1) space?
#
# Note: In python, strings are immutable so you have to introduce another string when removing the applying
# backspace

# import re
#
#
# def apply_backspace(s):
#     while '#' in s:
#         s = s.lstrip('#')
#         pattern = re.compile(r'[a-z]#')
#         s = pattern.sub('', s)
#     return s

# def apply_backspace(s):
#     s = s.lstrip('#')
#     result = ''
#     i = 0
#     while i < len(s):
#         if s[i] != '#':
#             if i == len(s) - 1:
#                 result += s[i]
#             elif s[i + 1] == '#':
#                 i += 1
#             elif s[i + 1] != '#':
#                 result += s[i]
#         else:
#             result = result[:-1]
#         i += 1
#     return result

def apply_backspace(s):
    stack = []
    for i in range(len(s)):
        if s[i] != '#':
            stack.append(s[i])
        elif stack:
            stack.pop()
    return ''.join(stack)


def backspace_compare(s, t):
    return apply_backspace(s) == apply_backspace(t)


# print(backspace_compare('ab#c', 'ad#c'))

print(apply_backspace('ab#c'))
# print(apply_backspace('ad#c'))
#
# print(apply_backspace('ab##'))
# print(apply_backspace('c#d#'))
#
# print(apply_backspace('a##c'))
# print(apply_backspace('#a#c'))
#
# print(apply_backspace('a#c'))
# print(apply_backspace('b'))
