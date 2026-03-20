class Solution(object):
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = set()
                
                # Collect elements in k x k submatrix
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])
                
                vals = sorted(vals)
                
                # If only one distinct value
                if len(vals) <= 1:
                    row.append(0)
                else:
                    min_diff = float('inf')
                    
                    # Check adjacent differences
                    for t in range(1, len(vals)):
                        min_diff = min(min_diff, abs(vals[t] - vals[t-1]))
                    
                    row.append(min_diff)
            
            ans.append(row)
        
        return ans