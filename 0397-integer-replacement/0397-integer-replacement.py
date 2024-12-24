class Solution:
    def integerReplacement(self, n: int) -> int:
        
        if n == 1:
            return 0
        elif n == 2 :
            return 1
        elif n == 3 :
            return 2
        
        if n % 4 == 0 :
            return 2 + self.integerReplacement(n//4)
        elif n % 4 == 1 :
            return 3 + self.integerReplacement(n//4)
        elif n % 4 == 2 :
            return 1 + self.integerReplacement(n//2)
        elif n % 4 == 3 :
            return 3 + self.integerReplacement((n//4 + 1))
        
        return -1
        
        
        
        