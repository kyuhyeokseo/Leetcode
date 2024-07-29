class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0 or x == 1 :
            return x
        elif n == 0 :
            return 1
        
    
        if n > 0 :
            return x ** n
        
        else :
            m = -n
            
            return (1/x) ** m