class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        L = len(nums)
        if L == 1 :
            #print(nums)
            #print(0)
            return 0
        
        elif L == 2 :
            if nums[0] > nums[1] :
                #print(nums)
                #print(0)
                return 0
            else :
                #print(nums)
                #print(1)
                return 1
        
        center_idx = int(L//2)
        idxL = self.findPeakElement(nums[:center_idx])
        idxR = self.findPeakElement(nums[center_idx:])
        
        maxL, maxR = nums[idxL], nums[center_idx + idxR]
        
        if maxL > maxR :
            #print(nums)
            #print(idxL)
            return idxL
        else :
            #print(nums)
            #print(center_idx + idxR)
            return center_idx + idxR
        
        
        
        
        
        