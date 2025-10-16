class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing and leading spaces
        s = s.strip()
        # Split the string into words
        words = s.split(" ")
        # Return the length of the last word
        return len(words[-1])
