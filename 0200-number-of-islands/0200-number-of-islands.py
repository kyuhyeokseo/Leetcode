class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.grid = grid
        
        self.M = len(grid)
        self.N = len(grid[0])
        
        cnt = 0
        for i in range(self.M) :
            for j in range(self.N) :
                if self.grid[i][j] == '1' :
                    cnt += 1
                self.dfs(i,j)
        
        return cnt
        
    def dfs(self, i, j) :
        
        if i>=0 and i<self.M and j>=0 and j<self.N:
        
            if self.grid[i][j] == '1' :
                self.grid[i][j] = '0'

                self.dfs(i, j-1)
                self.dfs(i, j+1)
                self.dfs(i-1, j)
                self.dfs(i+1, j)

        