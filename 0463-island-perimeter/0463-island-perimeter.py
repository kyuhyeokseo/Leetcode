class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])
        ret = 0

        # Vertical
        for i in range(M):
            for j in range(N+1):
                if j==0 and grid[i][j]==1:
                    ret += 1
                elif j>0 and j<N and (grid[i][j-1]+grid[i][j]==1):
                    ret += 1
                elif j==N and grid[i][j-1]==1:
                    ret += 1
        
        # Horizontal
        for i in range(M+1):
            for j in range(N):
                if i==0 and grid[i][j]==1:
                    ret += 1
                elif i>0 and i<M and (grid[i-1][j]+grid[i][j]==1):
                    ret += 1
                elif i==M and grid[i-1][j]==1:
                    ret += 1

        return ret
