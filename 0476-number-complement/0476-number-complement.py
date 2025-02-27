import math

class Solution:
    def findComplement(self, num: int) -> int:
        
        N = int(math.log2(num))+1
        X = (1<<N) -1
        ret = X ^ num
        return ret

        
