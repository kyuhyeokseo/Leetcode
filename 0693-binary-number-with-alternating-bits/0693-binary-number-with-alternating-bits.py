class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        curr = n % 2

        while n:
            n = n >> 1
            tmp = n % 2
            if tmp == curr:
                return False
            curr = tmp
        
        return True