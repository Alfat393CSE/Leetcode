class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        from collections import deque
        
        visited = set()
        queue = deque([s])
        smallest = s
        
        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            
            # Update smallest lexicographically
            if curr < smallest:
                smallest = curr

            # Operation 1: Add 'a' to all digits at odd indices
            s_list = list(curr)
            for i in range(1, len(s_list), 2):
                s_list[i] = str((int(s_list[i]) + a) % 10)
            added = ''.join(s_list)

            # Operation 2: Rotate right by b positions
            rotated = curr[-b:] + curr[:-b]
            
            # Add new states to queue
            queue.append(added)
            queue.append(rotated)
        
        return smallest
