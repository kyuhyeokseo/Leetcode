class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        diff = x ^ y
        ret = 0
        while diff > 0 :
            ret += (diff & 1)
            diff >>= 1
        return ret