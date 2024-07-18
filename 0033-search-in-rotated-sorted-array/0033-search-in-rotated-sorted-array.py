class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = len(nums)
        if L == 1 :
            if nums[0] == target :
                return 0
            else :
                return -1
        
        elif L == 2 :
            if nums[0] == target :
                return 0
            elif nums[1] == target :
                return 1
            else :
                return -1
        
        center_idx = int(L//2)
        
        if nums[:center_idx][0] <= nums[:center_idx][-1] :
            if nums[:center_idx][0] > target or nums[:center_idx][-1] < target :
                idxL = -1
                idxR = self.search(nums[center_idx:], target)
            else :
                idxL = self.search(nums[:center_idx], target)
                idxR = self.search(nums[center_idx:], target)
                
        elif nums[center_idx:][0] <= nums[center_idx:][-1] :
            if nums[center_idx:][0] > target or nums[center_idx:][-1] < target :
                idxL = self.search(nums[:center_idx], target)
                idxR = -1
            else :
                idxL = self.search(nums[:center_idx], target)
                idxR = self.search(nums[center_idx:], target)
        
        else :
            idxL = self.search(nums[:center_idx], target)
            idxR = self.search(nums[center_idx:], target)
        
        
        if idxL >= 0 :
            return idxL
        elif idxR >= 0 :
            return center_idx + idxR
        else :
            return -1
        
        