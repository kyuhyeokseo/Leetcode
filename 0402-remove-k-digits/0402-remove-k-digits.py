class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        if len(num) == k :
            return '0'
        
        stk = []
        
        for n in num :
            
            while stk and k > 0 and stk[-1] > n:
                stk.pop()
                k -= 1
            stk.append(n)
        
        if k > 0 :
            stk = stk[:-k]
        
        ret = ''.join(stk).lstrip('0')
        
        return ret if ret else '0'
        
        
        
        
        
        