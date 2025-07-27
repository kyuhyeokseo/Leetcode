class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        if k == 0:
            return 1

        N, K = n, k
        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K+1)]

        for m in range(N):
            for n in range(N):
                dp[0][m][n] = 1
        
        for k in range(1, K+1):
            for m in range(N):
                for n in range(N):

                    for dm, dn in [[1,-2], [1,2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]:
                        x, y = m+dm, n+dn
                        if x>=0 and x<N and y>=0 and y<N:

                            dp[k][m][n] += 0.125 * dp[k-1][x][y]
        
        return dp[K][row][column]
