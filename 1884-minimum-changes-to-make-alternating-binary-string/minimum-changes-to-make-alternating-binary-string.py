class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        change_start_0 = 0
        change_start_1 = 0

        for i in range(len(s)):
            # expected characters
            if i % 2 == 0:
                if s[i] != '0':
                    change_start_0 += 1
                if s[i] != '1':
                    change_start_1 += 1
            else:
                if s[i] != '1':
                    change_start_0 += 1
                if s[i] != '0':
                    change_start_1 += 1

        return min(change_start_0, change_start_1)