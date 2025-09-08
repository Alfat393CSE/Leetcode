class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of tuples (value, Roman numeral) in descending order
        val_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        for value, roman in val_to_roman:
            # Append as many times as we can subtract 'value' from 'num'
            while num >= value:
                result += roman
                num -= value
                
        return result
sol = Solution()
print(sol.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(sol.intToRoman(58))    # Output: "LVIII"
print(sol.intToRoman(1994))  # Output: "MCMXCIV"
