class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 :
            return 0
        
        else :
            
            for i in range(1, x+5, 1):
                
                if i * i > x :
                    return i-1
        
        
        
        