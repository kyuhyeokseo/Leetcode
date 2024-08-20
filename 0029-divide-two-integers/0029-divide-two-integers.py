class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        A = dividend / divisor
        
        flag = ( (dividend >= 0) == (divisor > 0))
        sign = 1 if flag else -1
        
        X = A * sign
        
        if flag :
            if A > (1<<31) -1 :
                return (1<<31) - 1
            else :
                return int(A)
        
        else :
            if X > (1<<31) :
                return -(1<<31)
            else :
                return sign * (int(X))
        
        
        
        