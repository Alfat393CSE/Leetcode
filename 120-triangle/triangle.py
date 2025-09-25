class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update current element with its value + min of the two adjacent elements below
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])

        # The top element will contain the minimum path sum
        return triangle[0][0]
