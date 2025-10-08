class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case: anything raised to 0 is 1
        if n == 0:
            return 1.0

        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        current_product = x

        # Fast exponentiation
        while n > 0:
            if n % 2 == 1:  # if n is odd
                result *= current_product
            current_product *= current_product  # square the base
            n //= 2  # divide exponent by 2

        return result
