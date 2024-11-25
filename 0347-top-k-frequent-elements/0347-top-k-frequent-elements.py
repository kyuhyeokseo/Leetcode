import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        q = []
        d = {}
        ans = []
        
        for n in nums :
            if n in d :
                d[n] += 1
            else :
                d[n] = 1
        
        for x in d.keys():
            print([-d[x], x])
            heapq.heappush(q, (-d[x], x))
        
        print('----------')
        for _ in range(k):
            y = heapq.heappop(q)
            print(y, y[1])
            ans.append(y[1])
        
        return ans
        
        
        
        
        