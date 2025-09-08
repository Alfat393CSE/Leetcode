class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary mapping Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over the Roman numeral from right to left
        for char in reversed(s):
            value = roman_map[char]
            
            # If current value is less than previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
                
            # Update previous value
            prev_value = value
        
        return total
sol = Solution()
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
