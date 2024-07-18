class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #print(f'nums : {nums}')
        
        L = len(nums)
        
        if L == 0 :
            return 0
        elif L == 1 :
            if nums[0] == target : 
                #print(0)
                return 0
            elif target < nums[0] :
                #print(0)
                return 0
            else :
                #print(1)
                return 1
        
        center_idx = int(L//2)
        
        center_num = nums[center_idx]
        
        if center_num == target :
            #print(center_idx)
            return center_idx
        
        elif target < center_num :
            #print(0)
            return self.searchInsert(nums[:center_idx], target)
        
        else :
            #print(center_idx - 1)
            return center_idx + self.searchInsert(nums[center_idx:], target)
        