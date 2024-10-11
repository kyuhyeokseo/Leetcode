class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        L = len(nums)
        D = {}
        
        for i in range(L) :
            
            num = nums[i]
            idx = num // (valueDiff+1)
            
            if idx in D :
                return True
            if idx-1 in D and abs(D[idx-1] - num) <= valueDiff :
                return True
            if idx+1 in D and abs(D[idx+1] - num) <= valueDiff :
                return True
        
            D[idx] = num
            if i >= indexDiff :
                del D[(nums[i-indexDiff] // (valueDiff+1))]
            
        return False
        
        
        