class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        ret = 1
        N = len(s)
        if N == 1:
            return ret
        
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1
        
        for diff in range(1, N):
            for i in range(N-diff):
                j = i + diff

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])

        return dp[0][-1]
