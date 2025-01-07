class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        M, N = len(heights), len(heights[0])

        Pac = [[False for _ in range(N)] for _ in range(M)]
        Atl = [[False for _ in range(N)] for _ in range(M)]

        L1 = []
        for i in range(M):
            L1.append([i, 0])
            Pac[i][0] = True
        for i in range(1,N):
            L1.append([0, i])
            Pac[0][i] = True
        
        while L1 :
            
            L1_tmp = []
            for item in L1 :
                x, y = item[0], item[1]
                for (dx, dy) in [[1,0], [-1,0], [0,1], [0,-1]]:
                    if 0 <= x+dx < M and 0 <= y+dy < N :
                        if Pac[x+dx][y+dy] == False and heights[x][y] <= heights[x+dx][y+dy] :
                            Pac[x+dx][y+dy] = True
                            L1_tmp.append([x+dx, y+dy])
            L1 = L1_tmp[:]
    

        L2 = []
        for i in range(M):
            L2.append([i, N-1])
            Atl[i][N-1] = True
        for i in range(N-1):
            L2.append([M-1, i])
            Atl[M-1][i] = True
        
        while L2 :
            
            L2_tmp = []
            for item in L2 :
                x, y = item[0], item[1]
                for (dx, dy) in [[1,0], [-1,0], [0,1], [0,-1]]:
                    if 0 <= x+dx < M and 0 <= y+dy < N :
                        if Atl[x+dx][y+dy] == False and heights[x][y] <= heights[x+dx][y+dy] :
                            Atl[x+dx][y+dy] = True
                            L2_tmp.append([x+dx, y+dy])
            L2 = L2_tmp[:]
        
        ret = []
        for i in range(M):
            for j in range(N):
                if Pac[i][j] and Atl[i][j] :
                    ret.append([i,j])
        return ret
