class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        for i in range(len(s)):
            target = s[i]
            if target == '(' or target == '{' or target == '[' :
                stk.append(target)
            elif target == ')' :
                if len(stk) == 0 :
                    return False
                cmp = stk.pop()
                if cmp != '(':
                    return False
            elif target == '}' :
                if len(stk) == 0 :
                    return False
                cmp = stk.pop()
                if cmp != '{':
                    return False
            elif target == ']' :
                if len(stk) == 0 :
                    return False
                cmp = stk.pop()
                if cmp != '[':
                    return False
            
        if len(stk) != 0 :
            return False
        
        return True
        
        
        
        
        
        