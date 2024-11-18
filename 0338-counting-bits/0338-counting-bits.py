import math

class Solution:
    def countBits(self, n: int) -> List[int]:
    
        if n == 0 :
            return [0]
        elif n == 1 :
            return [0,1]
    
        out = [0, 1]
        
        maxTwo = int(math.log2(n))
        
        limit = 2
        for X in range(2, n+1) :
            if X == 2 * limit :
                limit = limit << 1
            
            if X >= limit and X < 2 * limit :
                R = out[X%limit]
                out.append(1+R)
            
        return out