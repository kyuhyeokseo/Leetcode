class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        out = 0
        
        for i in range(31, -1, -1) :
            
            test = (right >> i)
            
            if (test % 2) == 0 :
                continue
            else :
                
                testLeft = (left >> i)
                if test <= testLeft :
                    out += (1 << i)
                
                
        return out    
        
        
        
        
        