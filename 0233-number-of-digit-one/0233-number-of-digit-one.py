class Solution:
    def countDigitOne(self, n: int) -> int:
        
        if n == 0 :
            return 0
        elif n < 10 :
            return 1
        
        n_str = str(n)
        L = len(n_str)
        
        cnt = 0
        
        for i in range(L):
            
            if i == 0 :
                if n_str[i] == '1' :
                    cnt += (int(n_str[1:])+1)
                else :
                    cnt += (10 ** (L-1))
            
            elif i > 0 and i < L-1 :
                
                cnt += (int(n_str[:i]) * (10 ** (L-1-i)))
                if n_str[i] == '0' :
                    cnt += 0
                elif n_str[i] == '1' :
                    cnt += (int(n_str[i+1:])+1)
                else :
                    cnt += (10 ** (L-1-i))
            
            else :
                cnt += (int(n_str[:i]))
                if n_str[i] > '0' :
                    cnt += 1
            
            #print(i, cnt)
            
        return cnt
                
                    
        
        
        
        
        
        