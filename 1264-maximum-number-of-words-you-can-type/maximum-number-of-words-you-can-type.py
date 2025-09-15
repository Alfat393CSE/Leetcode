class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)   # store broken keys for O(1) lookup
        words = text.split()          # split text into words
        count = 0

        for word in words:
            if all(ch not in broken for ch in word):  # word is valid if no broken letter
                count += 1

        return count
s = Solution()
print(s.canBeTypedWords("hello world", "ad"))  # Output: 1
print(s.canBeTypedWords("leet code", "lt"))    # Output: 1
print(s.canBeTypedWords("leet code", "e"))     # Output: 0
