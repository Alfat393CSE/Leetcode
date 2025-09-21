class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: empty needle always returns 0
        if needle == "":
            return 0
        
        # Use built-in string find (efficient)
        return haystack.find(needle)
s = Solution()
print(s.strStr("sadbutsad", "sad"))   # Output: 0
print(s.strStr("leetcode", "leeto"))  # Output: -1
