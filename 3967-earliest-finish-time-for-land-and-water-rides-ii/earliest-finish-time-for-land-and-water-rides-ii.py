from bisect import bisect_right

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """

        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x[0] for x in rides]
            d = [x[1] for x in rides]
            n = len(rides)

            # prefix minimum duration
            pref = [0] * n
            pref[0] = d[0]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], d[i])

            # suffix minimum (start + duration)
            suff = [0] * n
            suff[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], s[i] + d[i])

            return s, pref, suff

        def query(t, starts, pref, suff):
            """
            min over rides of max(t, start) + duration
            """
            n = len(starts)
            pos = bisect_right(starts, t)

            ans = float('inf')

            # rides with start <= t
            if pos > 0:
                ans = min(ans, t + pref[pos - 1])

            # rides with start > t
            if pos < n:
                ans = min(ans, suff[pos])

            return ans

        # Preprocess water rides
        wStarts, wPref, wSuff = build(waterStartTime, waterDuration)

        ans = float('inf')

        # Land -> Water
        for ls, ld in zip(landStartTime, landDuration):
            land_finish = ls + ld
            ans = min(ans, query(land_finish, wStarts, wPref, wSuff))

        # Preprocess land rides
        lStarts, lPref, lSuff = build(landStartTime, landDuration)

        # Water -> Land
        for ws, wd in zip(waterStartTime, waterDuration):
            water_finish = ws + wd
            ans = min(ans, query(water_finish, lStarts, lPref, lSuff))

        return ans