class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def is_no_zero(x):
            return '0' not in str(x)
        
        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]

sol = Solution()
print(sol.getNoZeroIntegers(2))   # Output: [1, 1]
print(sol.getNoZeroIntegers(11))  # Output: [2, 9] or [3, 8]
