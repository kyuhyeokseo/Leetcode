class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        AVG = target / 4
        L = len(nums)
        
        result = []
        
        for x in range(L-3) :
            
            if x > 0 :
                if nums[x-1] == nums[x] :
                    continue
            
            if nums[x] + nums[x+1] + nums[x+2] + nums[x+3] > target :
                break
            
            for y in range(x+1, L-2) :
                
                if y > x+1 :
                    if nums[y-1] == nums[y] :
                        continue
                
                if nums[x] + nums[y] + nums[y+1] + nums[y+2] > target :
                    break
                
                z, w = y+1, L-1
                
                while z < w :
                    
                    tmp = nums[x] + nums[y] + nums[z] + nums[w]
                    if tmp < target :
                        z += 1
                    elif tmp > target :
                        w -= 1
                    else :
                        result.append([nums[x],nums[y], nums[z], nums[w]])
                        
                        while nums[z] == nums[z+1] :
                            z += 1
                            if z == L-1 :
                                break
                        
                        while nums[w] == nums[w-1] :
                            w -= 1
                            if w == y+1 :
                                break
                        
                        z += 1
                        w -= 1
        
        return result
                
                
                
        
        
        
        