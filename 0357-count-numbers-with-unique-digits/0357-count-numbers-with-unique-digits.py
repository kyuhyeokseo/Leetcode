class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0 :
            return 1
        
        cnt = 1
        S = 9
        
        for i in range(1, n+1):
            cnt += S
            S *= (10-i)
            
        return cnt
        
        
        
        
        