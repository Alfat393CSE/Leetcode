class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = [words[0]]  # Start with the first word

        for i in range(1, len(words)):
            # Compare sorted versions of current and last kept word
            if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])

        return res
