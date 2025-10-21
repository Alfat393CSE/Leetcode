class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the last digit and move backward
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry needed, done!
            digits[i] = 0  # Set to 0 if it was 9 and continue

        # If all digits were 9, we need to add one more digit at the front
        return [1] + digits
