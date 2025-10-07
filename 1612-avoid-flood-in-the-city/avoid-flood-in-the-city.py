import bisect

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [-1] * n
        full = {}          # lake -> day it was last filled
        dry_days = []      # indices of days where rains[i] == 0

        for i, lake in enumerate(rains):
            if lake == 0:
                # We can choose a lake to dry later
                bisect.insort(dry_days, i)
                ans[i] = 1  # Temporary value; we’ll update if we decide a lake to dry
            else:
                # It rains on lake
                if lake in full:
                    # Find a dry day after the last time this lake was filled
                    last_fill_day = full[lake]
                    pos = bisect.bisect_right(dry_days, last_fill_day)
                    if pos == len(dry_days):
                        # No dry day available -> flood
                        return []
                    dry_day = dry_days.pop(pos)
                    ans[dry_day] = lake  # Dry this lake on that dry day
                full[lake] = i
                ans[i] = -1  # Raining day always -1

        return ans
