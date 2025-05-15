class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        dp = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        self.M = m
        self.N = n
        self.MOD = 10 ** 9 + 7

        return self.find(maxMove, startRow, startColumn, dp)

    def find(self, maxMove, x, y, dp):
        if x < 0 or x >= self.M or y < 0 or y >= self.N:
            return 1
        
        if maxMove <= 0:
            return 0

        if dp[x][y][maxMove] is not None:
            return dp[x][y][maxMove]
        
        ret = 0
        ret += (self.find(maxMove-1, x+1, y, dp) % self.MOD)
        ret += (self.find(maxMove-1, x-1, y, dp) % self.MOD)
        ret += (self.find(maxMove-1, x, y-1, dp) % self.MOD)
        ret += (self.find(maxMove-1, x, y+1, dp) % self.MOD)

        dp[x][y][maxMove] = (ret % self.MOD)

        return ret % self.MOD