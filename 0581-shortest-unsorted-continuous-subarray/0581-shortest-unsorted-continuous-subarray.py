class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        L = len(nums)

        max_val = -100001
        max_idx = 0
        for i in range(L):
            if nums[i] >= max_val:
                max_val = nums[i]
            else:
                max_idx = i
        
        min_val = 100001
        min_idx = L-1
        for j in range(L-1, -1, -1):
            if nums[j] <= min_val:
                min_val = nums[j]
            else:
                min_idx = j
        
        if min_idx >= max_idx:
            return 0
        else :
            return max_idx - min_idx + 1