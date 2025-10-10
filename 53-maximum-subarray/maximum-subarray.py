class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current = max_global = nums[0]
        
        for i in range(1, len(nums)):
            # Either start new subarray at nums[i] or extend the previous one
            max_current = max(nums[i], max_current + nums[i])
            # Update global maximum if current is greater
            if max_current > max_global:
                max_global = max_current
        
        return max_global
