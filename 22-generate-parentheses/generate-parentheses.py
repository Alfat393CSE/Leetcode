class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(current, open_count, close_count):
            # If the current string is complete, add to result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # If we can add an open parenthesis, do it
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # If we can add a close parenthesis, do it
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Start backtracking with empty string and counts 0
        backtrack("", 0, 0)
        return result

# Example usage:
sol = Solution()
print(sol.generateParenthesis(3))
