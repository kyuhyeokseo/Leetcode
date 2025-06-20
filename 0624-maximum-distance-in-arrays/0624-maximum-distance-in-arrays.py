class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        ret = 0
        m, M = arrays[0][0], arrays[0][-1]
        for array in arrays[1:]:
            ret = max(abs(array[0] - M), abs(array[-1] - m), ret)
            m = min(m, array[0])
            M = max(M, array[-1])
        
        return ret
