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


def checkValidString(s):
    if set(s) == {'*'}:
        return True

    if '*' in s:
        r = s.count('*')
        for comb in combinations_with_replacement(['', '(', ')'], r):
            new_str = ''
            j = -1
            for c in s:
                if c == '*':
                    j += 1
                    new_str += comb[j]
                else:
                    new_str += c
            if valid_paren(new_str):
                return True
    else:
        return valid_paren(s)


def valid_paren(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
    return len(stack) == 0


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


print(checkValidString('*'))
print(checkValidString('**'))
print(checkValidString('()'))
print(checkValidString('(())'))
print(checkValidString('()()'))

print(checkValidString('*)()'))
print(checkValidString('(*()'))
print(checkValidString('()*)'))
print(checkValidString('()(*'))

print(checkValidString('()**'))
print(checkValidString('**()'))
print(checkValidString('(***'))
print(checkValidString('***)'))

print(checkValidString('(*)'))
