class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans = float('inf')

        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(m):
                water_finish = waterStartTime[j] + waterDuration[j]

                # Land -> Water
                finish1 = max(waterStartTime[j], land_finish) + waterDuration[j]

                # Water -> Land
                finish2 = max(landStartTime[i], water_finish) + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans