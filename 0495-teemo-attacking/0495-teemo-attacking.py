class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        i = 0
        curr = timeSeries[i]
        prev = curr
        ret = 0

        while i < len(timeSeries):
            
            curr += duration
            i += 1
            if i < len(timeSeries) and curr >= timeSeries[i]:
                curr = timeSeries[i]
            else:
                ret += (curr - prev)
                if i < len(timeSeries):
                    curr = timeSeries[i]
                    prev = curr

            #print(ret, curr, i)
        
        return ret
