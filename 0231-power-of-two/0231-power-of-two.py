class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0 :
            return False
        
        elif n == 1 :
            return True
        
        while n > 1 :
            if n%2 == 1 :
                return False
            n //= 2
        
        return True
        
        
        
        
        
        