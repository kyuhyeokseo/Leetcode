import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        K = len(nums)
        
        ret = [-100001, 100001]

        min_heap = []
        MAX = -100001
        for k in range(K):
            heapq.heappush(min_heap, (nums[k][0], k))
            MAX = max(MAX, nums[k][0])
            nums[k].pop(0)
        
        while True:
            min_val, min_idx = heapq.heappop(min_heap)
            if ret[1] - ret[0] > MAX - min_val:
                ret = [min_val, MAX]
            
            if nums[min_idx]:
                heapq.heappush(min_heap, (nums[min_idx][0], min_idx))
                MAX = max(MAX, nums[min_idx][0])
                nums[min_idx].pop(0)
            else:
                return ret

            #print(ret, '[',min_val, MAX,']', min_val, min_idx)
        
        
            
