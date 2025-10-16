from collections import Counter

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        count = Counter(((num % value) + value) % value for num in nums)
        mex = 0

        while True:
            rem = mex % value
            if count[rem] > 0:
                count[rem] -= 1
                mex += 1
            else:
                return mex
