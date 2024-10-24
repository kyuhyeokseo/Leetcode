# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        step = n//2
        srt = n - step
        
        F, T = 0, n
        
        while True :
            if isBadVersion(srt) :
                if T == srt :
                    return srt
                T = srt
                if step > 1 :
                    step = step // 2
                srt -= step
            
            else :
                if F == srt :
                    return srt + 1
                F = srt
                if step > 1 :
                    step = step // 2
                srt += step