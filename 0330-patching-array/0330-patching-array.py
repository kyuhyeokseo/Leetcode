class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        test = 1
        
        idx = 0
        cnt = 0
        
        while test <= n :
            
            if idx < len(nums) and nums[idx] <= test :
                test += nums[idx]
                idx += 1
            else :
                test += test
                cnt += 1
            
        return cnt
            
        
        
        
        
        
        