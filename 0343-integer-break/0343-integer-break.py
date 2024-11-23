class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n == 2 :
            return 1
        
        if n == 3 :
            return 2
        
        if n == 4 :
            return 4
        
        
        Q = n // 3
        R = n % 3
        
        if R == 0 :
            return 3 ** Q
        elif R == 1 :
            return (3 ** (Q-1)) * 4
        else :
            return (3 ** Q) * 2