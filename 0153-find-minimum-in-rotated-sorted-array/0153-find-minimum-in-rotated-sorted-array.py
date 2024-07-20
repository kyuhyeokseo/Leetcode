class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L = len(nums)
        
        if L == 1 :
            return nums[0]
        
        elif L == 2 :
            return min(nums[0], nums[1])
        
        else :
            if nums[0] < nums[-1] :
                return nums[0]
            else :
                
                center_idx = int(L//2)
                minL = self.findMin(nums[:center_idx])
                minR = self.findMin(nums[center_idx:])
                return min(minL, minR)
        
        
        