import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        N = int(math.sqrt(area))
        
        for n in range(N, 0, -1):
            if area % n == 0:
                return [area//n, n]



