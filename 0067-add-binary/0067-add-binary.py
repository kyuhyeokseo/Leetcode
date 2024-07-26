class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) >= len(b) :
            long = a
            short = b
        else :
            long = b
            short = a
            
        LL = len(long)
        L = len(short)
        
        ans = ""
        C = 0    
    
        for i in range(LL) :
            
            X = ord(long[LL-1-i]) - ord('0')
            
            if i < L :
                Y = ord(short[L-1-i]) - ord('0')
            else :
                Y = 0
            
            Z = X + Y + C
            
            R = Z%2
            C = Z//2
            
            ans = str(R) + ans
        
        if C == 1 :
            ans = str(1) + ans
        
        return ans

        
        
        
        
        