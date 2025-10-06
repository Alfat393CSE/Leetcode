class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])  # append a copy of nums
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)  # recurse
                nums[start], nums[i] = nums[i], nums[start]  # backtrack (undo swap)

        backtrack()
        return result
sol = Solution()
print(sol.permute([1, 2, 3]))
