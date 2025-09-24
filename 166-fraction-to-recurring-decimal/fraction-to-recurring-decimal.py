class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        res = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)

        res.append(".")

        # Dictionary to store remainder -> position mapping
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                # Insert '(' at the index of first occurrence
                res.insert(remainder_map[remainder], "(")
                res.append(")")
                break

            remainder_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)
