class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)   # dp[i] = new people who learn the secret on day i
        dp[1] = 1            # Day 1: one person learns the secret
        
        share = 0            # how many can share on this day
        
        for day in range(2, n + 1):
            # People who become eligible to share today
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # People who forget today, remove their contribution
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            
            # New people who learn today = those who share today
            dp[day] = share
        
        # Count people who still remember the secret at day n
        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans = (ans + dp[day]) % MOD
        
        return ans
