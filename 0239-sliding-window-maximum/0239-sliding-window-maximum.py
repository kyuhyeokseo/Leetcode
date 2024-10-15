import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        isin_D = {}
        
        L = len(nums)
        q = []
        ans = []

        for i in range(L):
            n = nums[i]
            
            if n in isin_D :
                isin_D[n] += 1
            else :
                isin_D[n] = 1
                
            heapq.heappush(q, -n)
            
            if i >= k :
                isin_D[nums[i-k]] -= 1
            
            if i >= k-1 :
                
                while isin_D[-q[0]] == 0 :
                    heapq.heappop(q)
                T = -q[0]
                ans.append(T)
        
        return ans
        
        
        
        