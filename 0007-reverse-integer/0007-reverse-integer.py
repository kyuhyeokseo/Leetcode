class Solution:
    def reverse(self, x: int) -> int:
        
        pos_flag = (x > 0)
        
        if pos_flag :
            n = x
        else :
            n = -x
        
        ans = 0
        
        while n > 0 :
            
            ans *= 10
            ans += (n%10)
            
            n = n // 10
        
        if (ans >> 31) > 0 :
            return 0
        
        
        if pos_flag :
            return ans
        else :
            return (-1) * ans
        
        
        
        
        
        
        
        