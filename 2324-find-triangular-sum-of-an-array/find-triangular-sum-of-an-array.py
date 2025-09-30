class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums
        return nums[0]
print(Solution().triangularSum([1,2,3,4,5]))  # Output: 8
print(Solution().triangularSum([5]))          # Output: 5

#Alfat