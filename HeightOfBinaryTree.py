# The height of a node in a tree is the number of edges on the longest simple
# downward path from the node to a leaf. The height of a tree is the height of its root.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def height(node):
    hleft = hright = 0
    if node.left:
        hleft = 1 + height(node.left)
    if node.right:
        hright = 1 + height(node.right)
    return max(hleft, hright)


def height_dfs(node):
    def dfs(curr, h):
        nonlocal maxh
        if curr.left:
            dfs(curr.left, h + 1)
        if curr.right:
            dfs(curr.right, h + 1)
        maxh = max(maxh, h)

    maxh = 0
    dfs(node, 0)
    return maxh


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

    assert height(node1) == height_dfs(node1) == 2
    assert height(node2) == height_dfs(node2) == 1
    assert height(node3) == height_dfs(node3) == 0
    assert height(node4) == height_dfs(node4) == 0
    assert height(node5) == height_dfs(node5) == 0

    ###
    node11 = TreeNode(11)
    node22 = TreeNode(22)
    node33 = TreeNode(33)
    node44 = TreeNode(44)
    assert height(node11) == height_dfs(node11) == 0

    node11.left = node22
    assert height(node11) == height_dfs(node11) == 1

    node22.left = node33
    assert height(node11) == height_dfs(node11) == 2

    node33.left = node44
    assert height(node11) == height_dfs(node11) == 3

    ###
    node111 = TreeNode(111)
    node222 = TreeNode(222)
    node333 = TreeNode(333)
    node444 = TreeNode(444)
    assert height(node111) == height_dfs(node111) == 0

    node111.right = node222
    assert height(node111) == height_dfs(node111) == 1

    node222.right = node333
    assert height(node111) == height_dfs(node111) == 2

    node333.right = node444
    assert height(node111) == height_dfs(node111) == 3
