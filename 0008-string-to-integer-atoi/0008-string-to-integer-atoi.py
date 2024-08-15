class Solution:
    def myAtoi(self, s: str) -> int:
        
        P = (1<<31) - 1
        N = -(1<<31)
        
        s = s.strip()
        
        L = len(s)
        
        sign = 1
        num = 0
        
        for i in range(L):
            
            if i == 0 and s[i] == '-' :
                sign = -1
                continue
                
            elif i == 0 and s[i] == '+' :
                sign = 1
                continue
                
            elif ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                num *= 10
                num += int(s[i])
                continue
            else :
                break
        
        if sign == 1 :
            
            if num <= P :
                return num
            else :
                return P
        else :
            if -num >= N :
                return -num
            else :
                return N
            
        
        
        