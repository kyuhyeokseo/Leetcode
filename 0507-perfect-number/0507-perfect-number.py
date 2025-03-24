import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        S = 0
        sqr = int(math.sqrt(num))

        for n in range(1, sqr+1):
            if num % n == 0:
                S += n
                if int(num/n) > n:
                    S +=  (num//n)
            if S > 2 * num:
                return False
        
        if S == 2 * num:
            return True
        else:
            return False