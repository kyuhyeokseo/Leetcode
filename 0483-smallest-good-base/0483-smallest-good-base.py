import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        
        n = int(n)

        for t in range(int(math.log(n, 2)), 1, -1):
            
            k = int( n ** (t ** -1))
            if n == (k ** (t+1) - 1) // (k - 1):
                return str(k)

        return str(n-1)