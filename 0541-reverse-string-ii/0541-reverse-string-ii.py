class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        ret = ''
        L = len(s)
        q = 0

        while q*k <= L:
            
            if (q+1) * k < L and q % 2 == 0:
                ret += s[q*k:(q+1)*k][::-1]
            elif (q+1) * k < L and q % 2 == 1:
                ret += s[q*k:(q+1)*k][:]
            elif (q+1) * k >= L and q % 2 == 0:
                ret += s[q*k:][::-1]
            elif (q+1) * k >= L and q % 2 == 1:
                ret += s[q*k:][:]
            
            q += 1
        
        return ret