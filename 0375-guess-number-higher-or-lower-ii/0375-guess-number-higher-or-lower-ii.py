class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        MAX = 999999999
        
        if n == 1 :
            return 0
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for j in range(2, n+1):
            for i in range(j-1, 0, -1):
                
                # i to j
                M = MAX
                for K in range(i, j+1):
                    left = 0 if K == i else dp[i][K-1]
                    right = 0 if K == j else dp[K+1][j]
                    M = min(M, max(left, right) + K)
                dp[i][j] = M
        
        return dp[1][n]
        