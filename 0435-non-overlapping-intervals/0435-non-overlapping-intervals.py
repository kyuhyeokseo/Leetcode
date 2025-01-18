import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        D = {}
        q = []

        for interval in intervals :
            srt = interval[0]
            end = interval[1]
            heapq.heappush(q, [end, -srt])
        
        last = -1000000
        cnt = 0

        while q :
            end, srt = heapq.heappop(q)
            srt = srt * -1

            if last <= srt :
                cnt += 1
                last = end
        return len(intervals) - cnt