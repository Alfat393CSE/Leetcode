class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        
        # Simulate the process from a starting index and direction
        def simulate(start, direction):
            arr = nums[:]
            curr = start
            dir = direction  # 1 for right, -1 for left
            
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir *= -1
                    curr += dir
            return all(x == 0 for x in arr)
        
        # Try all positions with nums[i] == 0 and both directions
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):  # moving right
                    res += 1
                if simulate(i, -1):  # moving left
                    res += 1
        
        return res
