import heapq
import math

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        q = []
        ans = []
        
        L1 = len(nums1)
        L2 = len(nums2)
        
        for i in range(L1) :
            heapq.heappush(q, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
            
        for _ in range(k) :
            S, X, Y, idx = heapq.heappop(q)
            ans.append([X, Y])
            
            if idx < L2-1 :
                heapq.heappush(q, (X+nums2[idx+1], X, nums2[idx+1], idx+1))
        
        return ans
        
        