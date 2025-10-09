class Solution(object):
    def minTime(self, skill, mana):
        """
        Optimized no-wait flow shop with O(n) space.
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n, m = len(skill), len(mana)
        if n == 0 or m == 0:
            return 0

        # Precompute total processing time for each potion
        total_time = [sum(skill[i] * mana[j] for i in range(n)) for j in range(m)]

        # s[j] = start time of potion j on wizard 0
        s = [0] * m

        # Compute start times (no waiting constraint)
        for j in range(m - 1):
            max_gap = float('-inf')
            sum_a = sum_b = 0
            for i in range(n):
                sum_a += skill[i] * mana[j]           # pref[i][j]
                if i > 0:
                    sum_b += skill[i - 1] * mana[j + 1]  # pref[i-1][j+1]
                gap = sum_a - sum_b
                if gap > max_gap:
                    max_gap = gap
            s[j + 1] = s[j] + max_gap

        # Makespan = max_j (start + total processing)
        makespan = max(s[j] + total_time[j] for j in range(m))
        return makespan
