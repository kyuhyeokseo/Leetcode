import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        L = len(nums)
        heapq.heapify(nums)
        
        for _ in range(L-k+1):
            out = heapq.heappop(nums)
            print(out)

        return out
        
        