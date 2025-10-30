class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        # 0 -> red, 1 -> white, 2 -> blue
        while mid <= high:
            if nums[mid] == 0:
                # swap nums[low] and nums[mid]
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                # swap nums[mid] and nums[high]
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
