class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        L = len(num)
        if L < 3 :
            return False
        
        maxL = L // 3
        
        for i in range(L-2):
            
            if (i+1) >= L-(i+1):
                continue
                
            if num[0] == '0' and i>0 :
                continue
            
            for j in range(i+1, L-1):
                if max(i+1, j-i) > L-j-1 :
                    continue
                
                if num[i+1] == '0' and j>i+1 :
                    continue
                
                num1 = int(num[:i+1])
                num2 = int(num[i+1:j+1])
                idx = j+1
                
                while True :
                    N = str(num1 + num2)
                    NL = len(N)
                    
                    if L-idx < NL :
                        break
                    
                    if num[idx:idx+NL] != N :
                        break
                    
                    if idx+NL == L :
                        return True
                    
                    num1 = num2
                    num2 = int(N)
                    idx += NL
                    
        return False
                        
                
        
        
        
        
        
        