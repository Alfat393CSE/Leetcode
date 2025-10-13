class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0  # The farthest index we can reach so far
        n = len(nums)

        for i in range(n):
            # If the current index is beyond our reach, we can't proceed
            if i > max_reach:
                return False
            
            # Update the farthest reachable index
            max_reach = max(max_reach, i + nums[i])
            
            # If we can already reach or pass the last index, return True early
            if max_reach >= n - 1:
                return True
        
        return True  # If loop finishes, we can reach the end
