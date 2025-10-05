class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, visited, prev_height):
            # Out of bounds or already visited or can't flow uphill
            if (r < 0 or r >= m or c < 0 or c >= n or
                (r, c) in visited or heights[r][c] < prev_height):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # Start DFS from all Pacific-border and Atlantic-border cells
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])       # Top row (Pacific)
            dfs(m - 1, c, atlantic, heights[m-1][c]) # Bottom row (Atlantic)
        
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])       # Left column (Pacific)
            dfs(r, n - 1, atlantic, heights[r][n-1]) # Right column (Atlantic)
        
        # Cells reachable from both oceans
        result = list(pacific & atlantic)
        
        return result
