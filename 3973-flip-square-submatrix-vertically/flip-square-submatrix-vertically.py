class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        # Iterate over half of the rows in the submatrix
        for i in range(k // 2):
            # Swap row (x + i) with row (x + k - 1 - i)
            for j in range(y, y + k):
                grid[x + i][j], grid[x + k - 1 - i][j] = \
                grid[x + k - 1 - i][j], grid[x + i][j]
        
        return grid