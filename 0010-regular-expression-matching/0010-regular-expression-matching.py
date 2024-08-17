class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        prev = None
        curr = None
        
        M = len(s)
        N = len(p)
        
        dp = [[False for _ in range(N+1)] for _ in range(M+1)]
        
        dp[0][0] = True
        
        for x in range(M+1):
            for y in range(1, N+1):
                
                if p[y-1] == '*' :
                    dp[x][y] = (dp[x][y-2]) or ( (x>0) and (p[y-2] == '.' or (p[y-2] == s[x-1])) and dp[x-1][y] )
                    
                else :
                    dp[x][y] = (x > 0) and (dp[x-1][y-1]) and (p[y-1] == '.' or s[x-1] == p[y-1])
       
        return dp[M][N]
            
        
        
        
        
        
        
        