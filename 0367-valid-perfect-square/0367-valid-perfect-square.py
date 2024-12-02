class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        L = len(str(num))
        
        if L%2 == 0 :
            high = 10**(L//2)
            low = 10**((L-2)//2) * 3
        else :
            high = 10**((L-1)//2) * 4
            low = 10**((L-1)//2)
        
        while low < high :
            #print(low, high)
            
            if low * low == num :
                return True
            if high * high == num :
                return True
            
            mid = (low+high)//2
            
            if mid == low or mid == high :
                return False
            
            if mid * mid == num :
                return True
            elif mid * mid < num :
                low = mid
            else :
                high = mid
        
        return False
        
        