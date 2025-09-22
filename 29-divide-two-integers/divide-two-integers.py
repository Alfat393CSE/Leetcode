class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        # Subtract divisor multiples using bit shifting
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp to 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
print(Solution().divide(10, 3))   # 3
print(Solution().divide(7, -3))   # -2
print(Solution().divide(-2147483648, -1))  # 2147483647 (clamped)
