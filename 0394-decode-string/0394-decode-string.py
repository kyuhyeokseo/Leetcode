class Solution:
    def decodeString(self, s: str) -> str:
        
        stk = []
        L = len(s)
        num = ''
        inp = ''
        
        for i in range(L):
            
            target = s[i]
            
            if target >= '0' and target <= '9' :
                num += target
            
            elif target == '[' :
                stk.append('N' + num)
                stk.append('[')
                num = ''
            
            elif target >= 'a' and target <= 'z' :
                stk.append(target)
            
            elif target == ']':
                
                X = ''
                while stk[-1] != '[':
                    X = stk.pop() + X
                stk.pop()
                
                it = int(stk.pop()[1:])
                X = X * it
                
                while stk and stk[-1] != '[':
                    
                    Z = stk.pop()
                    if Z[0] == 'N' :
                        X = X * int(Z[1:])
                    else :
                        X = Z + X
                
                stk.append(X)
                
            else :
                return False
            
            #print(stk)
        
        return ''.join(stk)
                
            
        
        
        
        
        
        