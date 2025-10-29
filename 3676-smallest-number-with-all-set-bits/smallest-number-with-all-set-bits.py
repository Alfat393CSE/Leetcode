class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Start with 1 and keep shifting left until we get a number >= n
        # A number with k set bits is of the form (1 << k) - 1, e.g.,
        # k=3 → 111 (binary) → 7
        x = 1
        while (1 << x) - 1 < n:
            x += 1
        return (1 << x) - 1
