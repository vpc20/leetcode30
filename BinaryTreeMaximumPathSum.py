# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in
# the tree along the parent-child connections. The path must contain at least one node and does not need
# to go through the root.
#
# Example 1:
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
#
# Example 2:
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42

# Definition for a binary tree node.
import sys
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def find_max_util(root):
#     if root is None:
#         return 0
#
#     l = find_max_util(root.left)
#     r = find_max_util(root.right)
#
#     max_single = max(max(l, r) + root.val, root.val)
#     max_top = max(max_single, l + r + root.val)
#
#     find_max_util.res = max(find_max_util.res, max_top)
#     return max_single


def max_path_sum(root):
    def find_max(root):
        nonlocal maxsum
        if root is None:
            return 0

        maxl = find_max(root.left)
        maxr = find_max(root.right)

        max_root = max(maxl + root.val, maxr + root.val, root.val)
        maxsum = max(maxsum, max_root, maxl + maxr + root.val)
        return max_root

    maxsum = -sys.maxsize
    find_max(root)
    return maxsum


def print_preorder(curr):
    print(curr.val)
    if curr.left is not None:
        print_preorder(curr.left)
    if curr.right is not None:
        print_preorder(curr.right)


# arr = [1, 2, 3]
arr = [-10, 9, 20, None, None, 15, 7]

# root = TreeNode(arr[0])
# q = deque([root])
# i = -1
# while q:
#     node = q.popleft()
#     i += 1
#
#     left_idx = i * 2 + 1
#     if left_idx < len(arr) and arr[i]:
#         node.left = TreeNode(arr[left_idx]) if arr[left_idx] else None
#         q.append(node.left)
#
#     right_idx = i * 2 + 2
#     if right_idx < len(arr) and arr[i]:
#         node.right = TreeNode(arr[right_idx]) if arr[right_idx] else None
#         q.append(node.right)


# nodes = []
# for v in arr:
#     if v:
#         nodes.append(TreeNode(v))
#     else:
#         nodes.append(None)
# root = nodes[0]
nodes = [TreeNode(v) if v else None for v in arr]
root = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(arr) and arr[i]:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(arr) and arr[i]:
        node.right = nodes[right_idx]

print_preorder(root)
print(max_path_sum(root))
