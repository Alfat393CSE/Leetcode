class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        # dp[i][j] = whether s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # Handle patterns like a*, a*b*, a*b*c* for empty string
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    # Current chars match
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # Case 1: Treat * as zero occurrence of prev char
                    dp[i][j] = dp[i][j - 2]

                    # Case 2: If previous char matches current s[i-1], use *
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
print(Solution().isMatch("aa", "a"))     # False
print(Solution().isMatch("aa", "a*"))    # True
print(Solution().isMatch("ab", ".*"))    # True
print(Solution().isMatch("mississippi", "mis*is*p*.")) # False
