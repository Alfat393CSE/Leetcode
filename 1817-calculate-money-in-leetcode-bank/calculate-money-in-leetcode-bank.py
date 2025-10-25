class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Number of complete weeks
        weeks = n // 7
        # Remaining days after complete weeks
        days = n % 7
        
        # Total for full weeks:
        # Each week starts with +1 from the previous one.
        # Formula for sum of first week = 1+2+3+4+5+6+7 = 28
        # For each next week, it increases by 7 (since each day increases by 1)
        total = (weeks * 28) + (7 * weeks * (weeks - 1)) // 2
        
        # Total for remaining days in the last incomplete week
        start = weeks + 1
        for i in range(days):
            total += start + i
        
        return total
