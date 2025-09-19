class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 0  # slow pointer (last unique element index)
        for j in range(1, len(nums)):  # fast pointer
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1  # number of unique elements
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k, nums[:k])  
# Output: 5 [0, 1, 2, 3, 4]
