class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Continue reducing the string until only two digits remain
        while len(s) > 2:
            new_s = ""
            for i in range(len(s) - 1):
                # Take sum of consecutive digits modulo 10
                new_digit = (int(s[i]) + int(s[i + 1])) % 10
                new_s += str(new_digit)
            s = new_s  # Replace s with the new sequence

        # Return True if the last two digits are equal, False otherwise
        return s[0] == s[1]
