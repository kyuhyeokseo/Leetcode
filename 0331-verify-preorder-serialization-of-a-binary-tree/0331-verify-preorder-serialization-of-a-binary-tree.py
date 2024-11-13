class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        P = preorder.split(',')
        
        stk = []
        
        for p in P :
            
            if p == '#' :
                stk.append(p)
                while len(stk) >= 3 and stk[-2] == '#' and stk[-3] != '#' :
                    stk.pop()
                    stk.pop()
                    stk.pop()
                    stk.append('#')
                    
            else :
                stk.append(p)
                
            #print(stk)
        
        #print('----------')
        #print(stk)
        
        if len(stk) == 1 and stk[0] == '#' :
            return True
        
        return False
        
        
        
        
        