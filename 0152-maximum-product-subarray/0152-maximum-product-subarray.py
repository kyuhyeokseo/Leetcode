class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        rev = nums[::-1]
        out = -99999
        
        tmp = 1
        tmp_rev = 1
        
        for i in range(len(nums)):
            num = nums[i]
            R = rev[i]
            
            tmp *= num
            tmp_rev *= R
            
            out = max(out, tmp, tmp_rev)
            if tmp == 0 :
                tmp = 1
            if tmp_rev == 0:
                tmp_rev = 1
        
            
        return out
        
        
        
        
        