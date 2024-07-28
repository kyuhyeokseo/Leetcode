class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y0 = x
        
        if x < 0 :
            return False
        
        if x == 0 :
            return True
        
        y = 0
        
        while x > 0 :
            y += (x%10)
            y *= 10
            x //= 10
        
        y = y//10
        
        return (y0==y)
        
        
        
        
        
        