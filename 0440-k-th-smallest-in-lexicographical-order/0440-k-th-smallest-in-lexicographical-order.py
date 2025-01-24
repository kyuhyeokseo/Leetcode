class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        ret = 1
        i = 1

        while i < k :
            req = self.getReqNum(ret, ret+1, n)
            if i + req <= k :
                i += req
                ret += 1
            else :
                i += 1
                ret *= 10
        return ret

    def getReqNum(self, srt, end, n):
        gap = 0
        while srt <= n :
            gap += min(end, n+1) - srt
            srt *= 10
            end *= 10
        return gap
