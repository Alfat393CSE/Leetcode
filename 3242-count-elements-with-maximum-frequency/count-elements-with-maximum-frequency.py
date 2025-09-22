class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        freq = Counter(nums)  # count occurrences
        max_freq = max(freq.values())  # find the maximum frequency
        total = sum(count for count in freq.values() if count == max_freq)  # sum only max freq elements
        return total
print(Solution().maxFrequencyElements([1,2,2,3,1,4]))  # Output: 4
print(Solution().maxFrequencyElements([1,2,3,4,5]))    # Output: 5
