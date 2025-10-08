import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Sort potions to use binary search
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            # Minimum potion strength required to reach 'success'
            required = (success + spell - 1) // spell  # equivalent to ceil(success / spell)

            # Find first index where potion >= required
            idx = bisect.bisect_left(potions, required)

            # All potions from idx to end are successful
            res.append(m - idx)

        return res
