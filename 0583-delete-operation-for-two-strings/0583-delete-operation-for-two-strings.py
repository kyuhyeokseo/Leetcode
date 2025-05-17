class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        L1, L2 = len(word1), len(word2)

        dp = [[0 for _ in range(L1+1)] for _ in range(L2+1)]

        for i in range(1, L1+1):
            for j in range(1, L2+1):
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else :
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        
        common = dp[-1][-1]

        return L1 + L2 - 2 * common

