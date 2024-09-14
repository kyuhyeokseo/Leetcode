class Solution:
    def numTrees(self, n: int) -> int:
        
        self.dp = [1] * (20)
        
        self.dp[1] = 1
        self.dp[2] = 2
        
        if n < 3 :
            return self.dp[n]
        
        else :
            
            for i in range(3, n+1) :
                
                tmp = 0
                for j in range(i):
                    tmp += self.dp[j] * self.dp[i-1-j]
                self.dp[i] = tmp
            
            return self.dp[n]
        
        
        