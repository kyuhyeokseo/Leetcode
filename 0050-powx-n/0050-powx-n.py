class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0 :
            return 1
        elif x == 0 or x == 1 :
            return x
        
        if n < 0 :
            x = 1/x
            n = -n

        
        out = 1.00
        
        while n > 0 :
            
            if (n&1 == 0) :
                x *= x
            else :
                out *= x
                x *= x
            
            n = n>>1
        
        return out
        