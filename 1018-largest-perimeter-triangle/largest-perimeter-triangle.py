class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort descending
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b + c > a:  # Triangle condition
                return a + b + c
        return 0
print(Solution().largestPerimeter([2,1,2]))   # Output: 5
print(Solution().largestPerimeter([1,2,1,10])) # Output: 0
print(Solution().largestPerimeter([3,6,2,3]))  # Output: 8
