# Alfat Tasnim Hasan
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        # If n is odd, include 0
        if n % 2 != 0:
            result.append(0)
        
        # Generate pairs of positive and negative numbers
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        return result

# Example usage:
sol = Solution()
print(sol.sumZero(5))  # Output: [0, 1, -1, 2, -2] or any permutation
print(sol.sumZero(3))  # Output: [0, 1, -1]
print(sol.sumZero(1))  # Output: [0]

        