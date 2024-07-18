class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        L = len(nums)
        
        if L == 0 :
            return [-1, -1]
        
        if L == 1 :
            if nums[0] == target :
                return [0, 0]
            else :
                return [-1, -1]
        
        center_idx = int(L//2)
        
        [srtL, endL] = self.searchRange(nums[:center_idx], target)
        [srtR, endR] = self.searchRange(nums[center_idx:], target)
        
        
        if srtL == -1 and srtR == -1 :
            srtRet = -1
        elif srtL == -1 and srtR >= 0 :
            srtRet = center_idx + srtR
        elif srtL >= 0 and srtR == -1 :
            srtRet = srtL
        else :
            srtRet = srtL
            
        
        if endL == -1 and endR == -1 :
            endRet = -1
        elif endL == -1 and endR >= 0 :
            endRet = center_idx + endR
        elif endL >= 0 and endR == -1 :
            endRet = endL
        else :
            endRet = center_idx + endR
        
        return [srtRet, endRet]
        
        
        
        
        
        
        