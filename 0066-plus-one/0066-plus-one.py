class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        L = len(digits)
        
        out = []
        
        C = 0
        
        for i in range(L-1, -1, -1) :
            
            if i == L-1 :
                R = (digits[i] + 1) % 10
                C = (digits[i] + 1) // 10
                out = [R] + out
            
            else :
                if C == 0 :
                    out = [digits[i]] + out
                    
                else :
                    R = (digits[i] + 1) % 10
                    C = (digits[i] + 1) // 10
                    out = [R] + out
        
        if C == 1 :
            out = [1] + out
            
        return out
        