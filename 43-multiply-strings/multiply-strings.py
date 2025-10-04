class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # If either number is "0", the result is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array of zeros (max possible length = len(num1) + len(num2))
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse both strings for easier calculation (units first)
        num1, num2 = num1[::-1], num2[::-1]

        # Multiply each digit and add to result
        for i in range(m):
            for j in range(n):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                result[i + j] += digit1 * digit2

                # Handle carry over
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert digits back to string
        return ''.join(str(x) for x in reversed(result))
