class Solution:
    def findNthDigit(self, n: int) -> int:
        
        L, U = 0, 0
        i = 1
        
        while not(L <= n and n <= U) :
            L = U + 1
            U += i * 9 * (10**(i-1))
            i += 1
        
        i -= 1
        #print(L, U, i)
        Q = (n-L) // i
        R = (n-L) % i
        
        target = (10 ** (i-1)) + Q
        
        return int(str(target)[R])
        
        
        
        
        
        
        