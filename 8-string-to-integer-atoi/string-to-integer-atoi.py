class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Trim leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Handle sign
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # Step 3: Parse digits
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)

        # Apply sign
        num *= sign

        # Step 4: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
sol = Solution()

print(sol.myAtoi("42"))          # 42
print(sol.myAtoi("   -042"))     # -42
print(sol.myAtoi("1337c0d3"))    # 1337
print(sol.myAtoi("0-1"))         # 0
print(sol.myAtoi("words 987"))   # 0
print(sol.myAtoi("91283472332")) # 2147483647 (clamped)
print(sol.myAtoi("-91283472332"))# -2147483648 (clamped)

#Alfat Tasnim Hasan
