class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        N = columnNumber - 1
        
        R = N % 26
        N = N // 26
        
        out = ''
        out = chr(ord('A') + R) + out
        
        while N > 0 :
            
            N -= 1
            R = N % 26
            N = N // 26
            
            out = chr(ord('A') + R) + out
            
            
        
        return out
        
        
        