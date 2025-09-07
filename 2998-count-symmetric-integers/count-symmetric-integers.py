class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:  # only even digit numbers
                n = len(s) // 2
                first_half = s[:n]
                second_half = s[n:]
                if sum(int(d) for d in first_half) == sum(int(d) for d in second_half):
                    count += 1
        return count

# Example usage:
sol = Solution()
print(sol.countSymmetricIntegers(1, 100))    # Output: 9
print(sol.countSymmetricIntegers(1200, 1230)) # Output: 4

        