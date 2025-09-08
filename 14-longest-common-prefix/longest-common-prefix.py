class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce prefix length until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last character
                if prefix == "":
                    return ""
        
        return prefix
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
print(sol.longestCommonPrefix(["interview","interval","internal"]))  # Output: "inte"
