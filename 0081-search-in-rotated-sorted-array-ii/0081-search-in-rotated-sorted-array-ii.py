class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        L = len(nums)
        
        if L == 1 :
            if target == nums[0] :
                return True
            else :
                return False
            
        elif L == 2 :
            if target == nums[0] or target == nums[1] :
                return True
            else :
                return False
        
        else :
            i = int((L-1)//2)
            
            #print((nums[0:i+1], nums[i+1:]))
            L1, L2, R1, R2 = nums[0], nums[i], nums[i+1], nums[-1]
            
            if L1 < L2 :
                if target == L1 or target == L2 :
                    return True
                else :
                    if target > L1 and target < L2 :
                        return self.search(nums[0:i+1], target)
                    else :
                        return self.search(nums[i+1:], target)
                    
            elif L1 == L2 :
                if target == L1 or target == L2 :
                    return True
                else :
                    return (self.search(nums[0:i+1], target) or self.search(nums[i+1:], target))
            
            else :
                if target == L1 or target == L2 :
                    return True
                else :
                    if target > L1 or target < L2 :
                        return self.search(nums[0:i+1], target)
                    else :
                        return self.search(nums[i+1:], target)
                    
                    
                    
                    
                    
                    