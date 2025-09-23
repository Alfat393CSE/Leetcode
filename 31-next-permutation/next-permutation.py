class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find first decreasing index i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # if such i exists
            # Step 2: Find index j where nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse from i+1 to end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
nums = [1,2,3]
Solution().nextPermutation(nums)
print(nums)  # [1,3,2]

nums = [3,2,1]
Solution().nextPermutation(nums)
print(nums)  # [1,2,3]

nums = [1,1,5]
Solution().nextPermutation(nums)
print(nums)  # [1,5,1]
