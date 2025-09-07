class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store number -> index
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                # Found the pair
                return [num_to_index[complement], i]
            # Store current number and its index
            num_to_index[num] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Output: [0, 1]
print(sol.twoSum([3,2,4], 6))      # Output: [1, 2]
print(sol.twoSum([3,3], 6))        # Output: [0, 1]
