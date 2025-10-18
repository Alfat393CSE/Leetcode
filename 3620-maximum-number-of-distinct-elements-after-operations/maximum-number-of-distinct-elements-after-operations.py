class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        next_free = -10**18  # very small start
        count = 0

        for num in nums:
            # Place this number as low as possible but still within [num - k, num + k]
            place = max(num - k, next_free)
            if place <= num + k:
                count += 1
                next_free = place + 1  # next available distinct number
        
        return count
