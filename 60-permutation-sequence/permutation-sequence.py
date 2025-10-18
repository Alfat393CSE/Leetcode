class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # convert to 0-based index
        res = ""
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            res += nums[index]
            nums.pop(index)
            k %= fact
        
        return res
# Alfat