class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        out = -99999
        
        tmp = 1
        for i in range(len(nums)):
            num = nums[i]
            tmp *= num
            out = max(out, tmp)
            if tmp == 0 :
                tmp = 1
        
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            tmp *= num
            out = max(out, tmp)
            if tmp == 0 :
                tmp = 1
            
        return out
        
        
        
        
        