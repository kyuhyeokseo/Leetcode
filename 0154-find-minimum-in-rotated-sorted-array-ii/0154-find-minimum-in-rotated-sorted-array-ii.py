class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return nums[0]
        
        elif len(nums) == 2 :
            return min(nums[0], nums[1])
        
        else :
            
            if nums[0] < nums[-1] :
                return nums[0]
            
            elif nums[0] == nums[-1] :
                
                mid_idx = (len(nums)-1)//2
                N = nums[mid_idx]
                if N > nums[0] :
                    return self.findMin(nums[mid_idx+1:])
                elif N == nums[0] :
                    leftMin = self.findMin(nums[:mid_idx+1])
                    rightMin = self.findMin(nums[mid_idx+1:])
                    return min(leftMin, rightMin)
                else :
                    return self.findMin(nums[:mid_idx+1])
            
            else :
                mid_idx = (len(nums)-1)//2
                N = nums[mid_idx]
                if N >= nums[0] :
                    return self.findMin(nums[mid_idx+1:])
                else :
                    return self.findMin(nums[:mid_idx+1])
        
        
        
        