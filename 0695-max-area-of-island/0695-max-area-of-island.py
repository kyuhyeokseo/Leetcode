class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ret = 0
        M, N = len(grid), len(grid[0])

        def findArea(x, y):
            if grid[x][y] == 0:
                return 0
            ret = 1
            grid[x][y] = 0
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x2, y2 = x+dx, y+dy
                if 0 <= x2 < M and 0 <= y2 < N:
                    ret += findArea(x2, y2)
            return ret



        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    ret = max(ret, findArea(m, n))

        return ret        


