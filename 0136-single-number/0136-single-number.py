class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        L = len(nums)
        
        if L==1 :
            return nums[0]
    
        else :
            
            out = nums[0]
            
            for i in range(1, L):
                out ^= nums[i]
                
            return out
        
        