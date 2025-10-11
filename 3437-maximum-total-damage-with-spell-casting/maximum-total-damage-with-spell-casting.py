class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        from collections import Counter
        import bisect

        if not power:
            return 0

        # total damage for each unique power
        count = Counter(power)
        damage = {x: x * count[x] for x in count}

        # sorted unique powers
        values = sorted(damage.keys())
        n = len(values)
        if n == 0:
            return 0
        if n == 1:
            return damage[values[0]]

        dp = [0] * n
        dp[0] = damage[values[0]]

        for i in range(1, n):
            # option 1: skip current
            skip = dp[i-1]

            # find the last index j < i with values[j] <= values[i] - 3
            # bisect_right returns insertion point; subtract 1 to get last <= target
            target = values[i] - 3
            j = bisect.bisect_right(values, target, 0, i) - 1

            take = damage[values[i]]
            if j >= 0:
                take += dp[j]

            dp[i] = max(skip, take)

        return dp[-1]
