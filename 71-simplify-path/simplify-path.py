class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Split the path by '/' to get components
        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '' or part == '.':
                # Skip empty parts (caused by //) or current directory '.'
                continue
            elif part == '..':
                # Go up one directory if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory or file name
                stack.append(part)

        # Join the stack with '/' to form canonical path
        return '/' + '/'.join(stack)
