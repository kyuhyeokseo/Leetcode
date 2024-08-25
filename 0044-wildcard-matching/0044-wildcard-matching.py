class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        Ls, Lp = len(s), len(p)
        
        dp = [[False for _ in range(Ls+1)] for _ in range(Lp+1)]
        
        dp[0][0] = True

        check = False
        
        for i in range(1, Lp+1):
            check = False
            pat = p[i-1]
            
            if pat != '*' and pat != '?' :
                for j in range(1, Ls+1) :
                    if s[j-1] == pat :
                        check = True
                        dp[i][j] = dp[i-1][j-1]

            elif pat == '?':
                for j in range(1, Ls+1) :
                    check = True
                    dp[i][j] = dp[i-1][j-1]
                
            else :
                for j in range(0, Ls+1):
                    for k in range(j+1):
                        if dp[i-1][k] == True :
                            check = True
                            dp[i][j] = dp[i-1][k]
            
            #print(check, pat)
            #for item in dp :
                #print(item)
            
            if check == False :
                return False
            
        #for item in dp :
            #print(item)
                            
                            
        return dp[-1][-1] 
            
            
            
        
            
            
        
        
        
        
        
        