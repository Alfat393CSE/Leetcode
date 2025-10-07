class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for word in strs:
            # Sort the word to use as a key (anagrams have the same sorted key)
            key = ''.join(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        # Return all grouped anagrams
        return list(anagrams.values())
