class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        # Transform s into a new string with separators to handle even-length palindromes
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n  # Array to store the radius of palindrome at each center
        center = 0
        right = 0
        max_len = 0
        max_center = 0

        for i in range(n):
            mirror = 2 * center - i  # Mirror of i around current center

            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand around center i
            a = i + p[i] + 1
            b = i - p[i] - 1
            while a < n and b >= 0 and t[a] == t[b]:
                p[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # Track the maximum palindrome
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        # Extract the longest palindrome from the original string
        start = (max_center - max_len) // 2
        return s[start:start + max_len]

# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"
