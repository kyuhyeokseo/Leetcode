class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        N = numerator / denominator
        
        flag = (numerator < 0) ^ (denominator < 0)
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        if float(N).is_integer():
            return str(int(N))
        
        X, Y = numerator, denominator
        
        Q = X // Y
        R = X % Y
        
        ans = ''
        
        D = {}
        
        while R > 0 and R not in D:
            D[R] = len(ans)
            R *= 10
            ans += str(R//Y)
            R = R % Y
        
        if R == 0 :
            out = str(Q) + '.' + ans
        else :
            out = str(Q) + '.' + ans[:D[R]] + '(' + ans[D[R]:] + ')'
        
        if flag == True :
            out = '-' + out
            
        return out
        
        
        
        
        
        