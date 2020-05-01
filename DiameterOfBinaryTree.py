# Diameter of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary
# tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through
# the root.
#
# Example:
# Given a binary tree
#
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def diameter(node):
    """
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.

    :param node: node of the tree
    :return: diameter of the tree
    """

    def dfs(curr):
        nonlocal maxval
        if curr.left is None and curr.right is None:
            return 0
        left = 0
        right = 0
        if curr.left:
            left = 1 + dfs(curr.left)
        if curr.right:
            right = 1 + dfs(curr.right)
        maxval = max(maxval, left + right)
        return max(left, right)

    if node is None:
        return 0
    maxval = 0
    dfs(node)
    return maxval


# def diameter(node):
#     def traverse(curr):
#         hleft = 0
#         hright = 0
#         if curr.left:
#             hleft = height(curr.left) + 1
#             traverse(curr.left)
#         if curr.right:
#             hright = height(curr.right) + 1
#             traverse(curr.right)
#         harr.append(hleft + hright)
#
#     if node is None:
#         return 0
#     harr = []
#     traverse(node)
#     return max(harr)


def height(node):
    """
    The height of a node in a tree is the number of edges on the longest simple
    downward path from the node to a leaf. The height of a tree is the height of its root.

    :param node: node of the tree
    :return: height of the node
    """
    left = 0
    right = 0
    if node.left:
        left = 1 + height(node.left)
    if node.right:
        right = 1 + height(node.right)
    return max(left, right)


# def diameterOfBinaryTree(self, root):
#     self.ans = 1
#
#     def depth(node):
#         if not node: return 0
#         L = depth(node.left)
#         R = depth(node.right)
#         self.ans = max(self.ans, L + R + 1)
#         return max(L, R) + 1
#
#     depth(root)
#     return self.ans - 1

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    assert diameter(node1) == 0

    node1.left = node2
    assert diameter(node1) == 1

    node1.right = node3
    print(diameter(node1))
    assert diameter(node1) == 2

    node2.left = node4
    assert diameter(node1) == 3

    node2.right = node5
    print(diameter(node1))
    assert diameter(node1) == 3

    # print(height(node1))
    # print(height(node2))
    # print(height(node3))
    # print(height(node4))
    # print(height(node5))
