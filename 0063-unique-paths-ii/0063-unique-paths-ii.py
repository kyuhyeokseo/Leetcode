class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        self.X = len(obstacleGrid)
        self.Y = len(obstacleGrid[0])
        
        
        dp = [[0 for _ in range(self.Y)] for _ in range(self.X)]
        
        if obstacleGrid[0][0] == 0 :
            dp[0][0] = 1
        
        for x in range(self.X) :
            for y in range(self.Y) :
                
                if x == 0 and y == 0 :
                    continue
                
                elif x == 0 and y!= 0 :
                    if obstacleGrid[x][y] == 0 :
                        dp[x][y] = dp[x][y-1]
                
                elif y == 0 and x!=0 :
                    if obstacleGrid[x][y] == 0 :
                        dp[x][y] = dp[x-1][y]
                
                else :
                    if obstacleGrid[x][y] == 0 :
                        dp[x][y] = dp[x-1][y] + dp[x][y-1]
                    else :
                        dp[x][y] = 0
        
        #for l in dp :
            #print(l)
        
        out = dp[-1][-1]
        return out
        