class Solution:
    def numDecodings(self, s: str) -> int:
        
        L = len(s)
        
        out = [0] * (L+1)
        out[0] = 1
        
        for i in range(1, L+1):
            
            if i == 1 :
                if s[0] == '0':
                    return 0
                else :
                    out[i] = 1
            
            else :
                if s[i-1] != '0':
                    out[i] += out[i-1]
                
                if s[i-2] == '1' :
                    out[i] += out[i-2]
                elif s[i-2] == '2' :
                    if int(s[i-1]) >= 0 and int(s[i-1]) <= 6 :
                        out[i] += out[i-2]
        
        #print(out)
        
        return out[-1]
        
        
        
        
        
        