import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        L = len(nums)
        q = []

        for n in nums :
            if n in q :
                continue
            
            if len(q) < 3 :
                heapq.heappush(q, n)
            else :
                MIN = q[0]
                if MIN < n :
                    heapq.heappop(q)
                    heapq.heappush(q, n)


        if len(q) < 3 :
            return max(q)

        else :
            return heapq.heappop(q)


