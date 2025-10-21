import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Trim whitespace
        s = s.strip()

        # Define regex pattern for a valid number
        pattern = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$')

        # Match and return True if valid, else False
        return bool(pattern.match(s))
