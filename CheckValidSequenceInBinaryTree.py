# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string
# is a valid sequence in such binary tree.
#
# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of
# the nodes along a path results in a sequence in the given binary tree.

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_preorder(curr):
    print(curr.val, end=' ')
    if curr.left is not None:
        print_preorder(curr.left)
    if curr.right is not None:
        print_preorder(curr.right)


# def is_valid_sequence(root, arr):
#     def dfs(curr, seq):
#         nonlocal result
#         if curr.left is None and curr.right is None:  # is a leaf
#             if seq == arr:
#                 result = True
#         if curr.left:
#             dfs(curr.left, seq + [curr.left.val])
#         if curr.right:
#             dfs(curr.right, seq + [curr.right.val])
#
#     result = False
#     dfs(root, [root.val])
#     return result


def is_valid_sequence(root, arr):
    def dfs(curr, seq):
        if curr.left is None and curr.right is None:  # is a leaf
            if seq == arr:
                return True
        if curr.left:
            if dfs(curr.left, seq + [curr.left.val]):
                return True
        if curr.right:
            if dfs(curr.right, seq + [curr.right.val]):
                return True
        return False

    return dfs(root, [root.val])


tree_arr = [0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]
# tree_arr = [0, 1, 0]
nodes = [TreeNode(v) if v is not None else None for v in tree_arr]
root = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(tree_arr) and tree_arr[i] is not None:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(tree_arr) and tree_arr[i] is not None:
        node.right = nodes[right_idx]
print_preorder(root)
print('')

arr = [0, 1, 0, 1]
# arr = [0, 1, 1, 0]
# arr = [1]
# arr = [0, 0]
# print(is_valid_sequence(root, arr))
assert is_valid_sequence(root, [0, 1, 0, 1]) == True
assert is_valid_sequence(root, [0, 1, 1, 0]) == True
assert is_valid_sequence(root, [0, 0, 0]) == True
assert is_valid_sequence(root, [0]) == False
assert is_valid_sequence(root, [1]) == False
assert is_valid_sequence(root, [0, 1, 1, 1]) == False
