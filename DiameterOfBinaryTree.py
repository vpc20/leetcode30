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

    @staticmethod
    def height(node):
        """
        The height of a node in a tree is the number of edges on the longest simple
        downward path from the node to a leaf, and the height of a tree is the
        height of its root.

        :param node: node of the tree
        :return: height of the node
        """

        def height_aux(curr, height):
            nonlocal max_height
            max_height = max(max_height, height)
            if curr.left:
                height_aux(curr.left, height + 1)
            if curr.right:
                height_aux(curr.right, height + 1)

        max_height = 0
        height_aux(node, 0)
        return max_height

    def diameter(self, node):
        def traverse(curr):
            hleft = 0
            hright = 0
            if curr.left:
                hleft = self.height(curr.left) + 1
                traverse(curr.left)
            if curr.right:
                hright = self.height(curr.right) + 1
                traverse(curr.right)
            harr.append(hleft + hright)

        if node is None:
            return 0
        harr = []
        traverse(node)
        return max(harr)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    # print(node1.height(node1))
    # print(node1.height(node2))
    # print(node1.height(node3))
    # print(node1.height(node4))
    # print(node1.height(node5))

    print(node1.diameter(node1))