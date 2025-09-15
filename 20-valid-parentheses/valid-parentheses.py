class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # if it's a closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)  # it's an opening bracket

        return not stack
print(Solution().isValid("()"))      # True
print(Solution().isValid("()[]{}"))  # True
print(Solution().isValid("(]"))      # False
print(Solution().isValid("([])"))    # True
print(Solution().isValid("([)]"))    # False
