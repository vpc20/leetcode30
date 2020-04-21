# (This problem is an interactive problem.)
#
# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted
# in non-decreasing order.
#
# Given a row-sorted binary matrix binary Matrix, return leftmost column index(0-indexed) with at least a 1 in it.
# If such index doesn't exist, return -1.
#
# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
#
#     BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
#     BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
#
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions
# that attempt to circumvent the judge will result in disqualification.
#
# For custom testing purposes you're given the binary matrix mat as input in the following four examples.
# You will not have access the binary matrix directly.
#
# Example 1:
# Input: mat = [[0,0],
#               [1,1]]
# Output: 0
#
# Example 2:
# Input: mat = [[0,0],
#               [0,1]]
# Output: 1
#
# Example 3:
# Input: mat = [[0,0],
#               [0,0]]
# Output: -1
#
# Example 4:
# Input: mat = [[0,0,0,1],
#               [0,0,1,1],
#               [0,1,1,1]]
# Output: 1
#
# Constraints:
#     1 <= mat.length, mat[i].length <= 100
#     mat[i][j] is either 0 or 1.
#     mat[i] is sorted in a non-decreasing way.


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#     def get(self, x: int, y: int) -> int:
#     def dimensions(self) -> list[]:

class BinaryMatrix:
    bin_matrix = []

    def get(self, x, y):
        return self.bin_matrix[x][y]

    def dimensions(self):
        return [len(self.bin_matrix), len(self.bin_matrix[0])]


def left_most_column_with_one(binary_matrix):
    numrows, numcols = binary_matrix.dimensions()
    col = numcols - 1  # last col
    for row in range(numrows):
        while col > -1 and binary_matrix.get(row, col) == 1:
            col -= 1
    return -1 if col == numcols - 1 else col + 1


# def left_most_column_with_one(binaryMatrix):
#     numrows, numcols = binaryMatrix.dimensions()
#     col = numcols - 1  # last col
#     start_row = -1
#
#     for row in range(numrows):
#         if start_row != -1:
#             break
#         for col in range(numcols):
#             if binaryMatrix.get(row, col) == 1:
#                 start_row = row
#                 break
#     if start_row == -1:
#         return -1
#
#     for row in range(start_row, numrows):
#         while col > -1 and binaryMatrix.get(row, col) == 1:
#             col -= 1
#     return col + 1
#

bm = BinaryMatrix()
bm.bin_matrix = [[0, 0, 0, 1],
                 [0, 0, 1, 1],
                 [0, 1, 1, 1]]
# bm.bin_matrix = [[0, 0],
#                  [0, 0]]


# print(bm.dimensions())
# print(bm.get(2, 3))
print(left_most_column_with_one(bm))
print(bm.dimensions())
