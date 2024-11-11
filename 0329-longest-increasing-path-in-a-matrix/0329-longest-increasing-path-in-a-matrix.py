class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        M, N = len(matrix), len(matrix[0])
        out = self.getLongest(M, N, matrix)
    
        return out
    
    
    def getLongest(self, M, N, matrix) :
        
        out = -1
        self.dp = [[-1] * N for _ in range(M)]
        
        for m in range(M):
            for n in range(N):
                out = max(out, self.mnFind(m, n, M, N, matrix))
            
        return out
    
    def mnFind(self, m, n, M, N, matrix):
        
        if self.dp[m][n] != -1 :
            return self.dp[m][n]
        
        out = 1
        direction = [[-1,0], [1,0], [0,-1], [0,1]]
        
        for d in direction :
            x, y = m+d[0], n+d[1]
            
            if x >= 0 and x < M and y >= 0 and y < N :
                if matrix[x][y] < matrix[m][n] :
                    
                    out = max(out, 1 + self.mnFind(x,y,M,N,matrix))
                    
        self.dp[m][n] = out
        return out
                    
            
        
        
        
        
        
        