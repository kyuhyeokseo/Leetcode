class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        L1, L2 = len(num1), len(num2)
        C = '0'
        ret = ''

        for i in range(max(L1, L2) + 1) :
            
            if i < L1 :
                s1 = num1[-1-i]
            else :
                s1 = '0'
            
            if i < L2 :
                s2 = num2[-1-i]
            else :
                s2 = '0'
            
            tmp = (ord(s1) + ord(s2) + ord(C) - 3 * ord('0'))
            C = str(tmp // 10)
            R = tmp % 10
            ret = str(R) + ret
        
        ret = ret.lstrip('0')
        if len(ret) == 0 :
            return '0'
        else :
            return ret