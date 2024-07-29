class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if n == 0 :
            return 0
        
        else :
            
            out = 0
            
            while n > 0 :
                out += (n//5)
                n = n//5
            
            return out