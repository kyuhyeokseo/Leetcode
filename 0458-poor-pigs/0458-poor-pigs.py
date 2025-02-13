class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        MAX_ITER = int(minutesToTest/minutesToDie)
        T = MAX_ITER + 1
        N = buckets

        ret = 0
        val = 1
        while val < N :
            ret += 1
            val *= T
        
        return ret