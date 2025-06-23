class Solution:

    def kInversePairs(self, n: int, k: int) -> int:
        N, K = n, k
        M = 1000000007
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

        if N == 1 and K >= 1:
            return 0
        elif N == 1:
            return 1

        dp[1][0] = 1
        for n in range(2, N+1):
            dp[n][0] = 1
        
        for n in range(2, N+1):
            for k in range(1, K+1):
                
                if k == 1:
                    dp[n][k] = n-1
                elif k-n < 0 and dp[n-1][k] > 0:
                    dp[n][k] = (dp[n][k-1] + dp[n-1][k]) % M
                elif k-n < 0:
                    dp[n][k] = dp[n][k-1]
                elif k-n >= 0 and dp[n-1][k] > 0:
                    dp[n][k] = (dp[n][k-1] + dp[n-1][k] - dp[n-1][k-n]) % M
                elif k-n >= 0 and dp[n-1][k] == 0 and dp[n-1][k-n] > 0:
                    dp[n][k] = (dp[n][k-1] - dp[n-1][k-n]) % M

        #for s in dp:
        #    print(s)

        return dp[N][K]


