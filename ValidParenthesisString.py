#  Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether
#  this string is valid. We define the validity of a string by these rules:
#
#     Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
#     An empty string is also valid.
#
# Example 1:
# Input: "()"
# Output: True
#
# Example 2:
# Input: "(*)"
# Output: True
#
# Example 3:
# Input: "(*))"
# Output: True
#
# Note:
#     The string size will be in the range [1, 100].
from itertools import combinations_with_replacement


# def check_valid_string(s):
#     if set(s) == {'*'}:
#         return True
#
#     if '*' in s:
#         r = s.count('*')
#         for comb in combinations_with_replacement(['', '(', ')'], r):
#             new_str = ''
#             j = -1
#             for c in s:
#                 if c == '*':
#                     j += 1
#                     new_str += comb[j]
#                 else:
#                     new_str += c
#             if valid_paren(new_str):
#                 return True
#     else:
#         return valid_paren(s)


# def valid_paren(s):
#     stack = []
#     for c in s:
#         if c == '(':
#             stack.append(c)
#         elif c == ')':
#             if not stack or stack[-1] != '(':
#                 return False
#             else:
#                 stack.pop()
#     return len(stack) == 0


# def valid_paren(s):
#     stack = 0
#     for c in s:
#         if c == '(':
#             stack += 1
#         elif c == ')':
#             if stack == 0:
#                 return False
#             else:
#                 stack -= 1
#     return stack == 0


# def checkValidString(s):
#     stack = []
#     star_stack = []
#     for i in range(len(s)):
#         if s[i] == '(':
#             stack.append(i)
#         elif s[i] == '*':
#             star_stack.append(i)
#         else:
#             if not stack and not star_stack:
#                 return False
#             if stack:
#                 stack.pop()
#             else:
#                 star_stack.pop()
#     while stack and star_stack:
#         if stack.pop() > star_stack.pop():
#             return False
#     return not stack

def check_valid_string(s):
    stack = 0
    for c in s:
        if c == '(' or c == '*':
            stack += 1
        else:
            if stack == 0:
                return False
            else:
                stack -= 1
    stack = 0
    for c in reversed(s):
        if c == ')' or c == '*':
            stack += 1
        else:
            if stack == 0:
                return False
            else:
                stack -= 1
    return True


print(check_valid_string('*'))
print(check_valid_string('**'))
print(check_valid_string('()'))
print(check_valid_string('(())'))
print(check_valid_string('()()'))

print(check_valid_string('*)()'))
print(check_valid_string('(*()'))
print(check_valid_string('()*)'))
print(check_valid_string('()(*'))

print(check_valid_string('()**'))
print(check_valid_string('**()'))
print(check_valid_string('(***'))
print(check_valid_string('***)'))

print(check_valid_string('(*)'))
