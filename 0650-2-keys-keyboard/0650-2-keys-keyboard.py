class Solution:
    def minSteps(self, n: int) -> int:
        
        ret = 0

        if n == 1:
            return ret
        
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return i + self.minSteps(n//i)
        
        return n
        
