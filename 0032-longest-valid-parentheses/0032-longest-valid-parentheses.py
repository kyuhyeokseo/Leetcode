from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        s = s.lstrip(')')
        s = s.rstrip('(')
        
        if len(s) == 0 or len(s) == 1 :
            return 0
        
        stk = deque()
        
        cnt = 0
        
        rec = [-1 for _ in range(len(s))]
        
        for i in range(len(s)) :
            
            if s[i] == '(' :
                stk.append([s[i], i])
            else :
                if stk :
                    ret = stk.pop()
                    tmp = i - ret[1] + 1
                    rec[ret[1]] = tmp
                    rec[i] = tmp
        
        split_list = list()
        
        x = -1
        out = 0
    
        for y in range(0, len(rec)):
            
            if rec[y] == -1 :
                
                if y == 0 :
                    x = y
                    continue
                else :
                    tmp_list = rec[x+1:y]
                    
                    #print(tmp_list)
                    L = len(tmp_list)
                    if L == 0 :
                        x = y
                        continue
                    m = 0
                    z = 0
                    while True :
                        #print(m)
                        if m + tmp_list[z] > L:
                            break
                        m += tmp_list[z]
                        z += tmp_list[z]
                        #print(m)
                        if z >= L :
                            break
                    
                    out = max(m, out)
                    x = y
        

        if x+1 < len(s):
            tmp_list = rec[x+1:]
                    
            L = len(tmp_list)
            m = 0
            z = 0
            while True :
                if m + tmp_list[z] > L:
                    break
                m += tmp_list[z]
                z += tmp_list[z]
                if z >= L :
                    break
                    
            out = max(m, out)
            #print(out)
  

        return out
        
        
        
        
        
        