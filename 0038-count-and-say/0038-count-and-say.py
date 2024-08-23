class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n==1 :
            return '1'
        
        s = '1'
        
        for _ in range(n-1):
            
            L = len(s)
            
            target = '-'
            cnt = 0
            s_tmp = ''
            
            for i in range(L):
                
                if target == s[i] :
                    cnt += 1
                
                else :
                    if target == '-' :
                        target = s[i]
                        cnt = 1
                    else :
                        s_tmp += (str(cnt) + str(target))
                        target = s[i]
                        cnt = 1
                        
            s_tmp += (str(cnt) + str(target))

            s = s_tmp[:]
        return s
    
        
            
            
            
        
        
        
        
        
        