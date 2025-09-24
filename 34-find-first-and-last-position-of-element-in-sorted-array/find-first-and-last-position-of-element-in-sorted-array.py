class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    index = mid
            return index

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    index = mid
            return index

        return [findLeft(nums, target), findRight(nums, target)]
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))  # [3, 4]
print(s.searchRange([5,7,7,8,8,10], 6))  # [-1, -1]
print(s.searchRange([], 0))              # [-1, -1]
