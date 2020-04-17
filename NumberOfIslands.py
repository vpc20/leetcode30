# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
# and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.
#
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3


def update_island(grid, row, col):
    grid[row][col] = '9'

    if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':  # right
        update_island(grid, row, col + 1)

    if row + 1 < len(grid) and grid[row + 1][col] == '1':  # down
        update_island(grid, row + 1, col)

    if col - 1 > -1 and grid[row][col - 1] == '1':  # left
        update_island(grid, row, col - 1)

    if row - 1 > -1 and grid[row - 1][col] == '1':  # up
        update_island(grid, row - 1, col)


def num_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                update_island(grid, i, j)
    return count


grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

# grid = [["1", "1", "0", "0", "0"],
#         ["1", "1", "0", "0", "0"],
#         ["0", "0", "1", "0", "0"],
#         ["0", "0", "0", "1", "1"]]

print(num_islands(grid))
