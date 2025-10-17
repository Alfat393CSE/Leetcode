class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the boundaries of the spiral
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        
        # Start filling numbers from 1 to n^2
        num = 1
        while left <= right and top <= bottom:
            # Move right → along the top row
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1  # move the top boundary down

            # Move down ↓ along the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # move the right boundary left

            # Move left ← along the bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1  # move the bottom boundary up

            # Move up ↑ along the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1  # move the left boundary right

        return matrix
