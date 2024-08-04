class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        self.MAX = (2<<24)
        self.M = len(grid)
        self.N = len(grid[0])
        
        self.grid = grid
        
        self.dp = [[self.MAX for _ in range(self.N)] for _ in range(self.M)]
        self.dp[0][0] = grid[0][0]
        
        for m in range(self.M) :
            for n in range(self.N) :
                self.propagation(m,n)
        
        return self.dp[-1][-1]
        
    def propagation(self, x, y):
        
        direc = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for idx in range(4) :
            dX, dY = direc[idx]
            
            if (x+dX >= 0) and (x+dX < self.M) and (y+dY >=0) and (y+dY < self.N) :
                self.dp[x+dX][y+dY] = min(self.dp[x+dX][y+dY], self.dp[x][y] + self.grid[x+dX][y+dY])
        
        
        