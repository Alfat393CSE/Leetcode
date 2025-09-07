class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If the character is already in the set, remove characters from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the new character and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
