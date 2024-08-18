class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        L = len(nums)
        
        out = nums[0] + nums[1] + nums[2]
        DIFF = abs(target - out)

        
        if DIFF == 0:
            return out
        
        for i in range(L-2) :
            #print(nums[i])
            
            if nums[i] + nums[i+1] + nums[i+2] >= target + abs(target - out) :
                return out
            
            j, k = i+1, L-1
            
            while j < k :

                tmp = nums[i] + nums[j] + nums[k]
                #print(tmp)
                if tmp < target :
                    j += 1
                    
                    if abs(target - tmp) < abs(target - out) :
                        out = tmp
                    
                elif tmp == target :
                    out = tmp
                    return out
                else :
                    k -= 1
                    if abs(target - tmp) < abs(target - out) :
                        out = tmp

            
        return out
                    
                    
                    
                    
                    
        
        
        
        
        