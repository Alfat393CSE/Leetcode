class Solution(object):
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # Initialize DP with very small values
        dp = [[[-10**15]*3 for _ in range(n)] for _ in range(m)]
        
        # Start position
        for k in range(3):
            if coins[0][0] < 0 and k > 0:
                dp[0][0][k] = 0  # neutralize
            else:
                dp[0][0][k] = coins[0][0]
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue
                    
                    val = coins[i][j]
                    
                    # From top
                    if i > 0:
                        # Take normally
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
                        
                        # Neutralize if negative
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                    
                    # From left
                    if j > 0:
                        # Take normally
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
                        
                        # Neutralize if negative
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        
        return max(dp[m-1][n-1])