class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        L = len(nums)
        for i in range(L):
            
            idx = nums[i]
            if idx < 0 :
                idx *= -1
            
            if nums[idx] < 0 :
                return idx
            else :
                nums[idx] *= -1
        
        
        
        
        
        
        