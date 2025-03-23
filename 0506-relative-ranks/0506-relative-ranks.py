import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        N = len(score)
        ret = [None] * N

        q = []
        heapq.heapify(q)

        for i, s in enumerate(score):
            heapq.heappush(q, (-s, i))
        
        for idx in range(N):
            _, i = heapq.heappop(q)
            if idx == 0:
                ret[i] = 'Gold Medal'
            elif idx == 1:
                ret[i] = 'Silver Medal'
            elif idx == 2:
                ret[i] = 'Bronze Medal'
            else:
                ret[i] = str(idx+1)
        
        return ret