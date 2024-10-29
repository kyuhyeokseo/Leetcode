class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def is_valid(p):
            
            N = 0
            for i in p :
                if i == '(':
                    N += 1
                elif i == ')':
                    N -= 1
                if N < 0 :
                    return False
                
            return N == 0
        
        ret = {s}
        if is_valid(s) :
            return [s]
        
        while True :
            F = filter(is_valid, ret)
            
            out = list(F)[:]
            
            if len(out) > 0 :
                return out
            
            ret = {ss[:i]+ss[i+1:] for ss in list(ret) for i in range(len(ss))}
            
        
        
        
        