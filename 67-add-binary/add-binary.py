class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1  # pointers for both strings (starting from rightmost bit)
        carry = 0
        result = []

        # loop while there are bits left in either string or carry is non-zero
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # add current bit to result
            result.append(str(total % 2))  # remainder gives current binary bit
            carry = total // 2  # integer division gives carry

        # reverse the result since we built it backwards
        return ''.join(reversed(result))
s = Solution()
print(s.addBinary("11", "1"))      # Output: "100"
print(s.addBinary("1010", "1011")) # Output: "10101"
