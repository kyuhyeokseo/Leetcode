class Solution:
    def rob(self, nums: List[int]) -> int:
        
        L = len(nums)
        
        record = []
        
        if L == 1 :
            return nums[0]
        elif L == 2 :
            return max(nums[0], nums[1])
        else :
            record = [0,0]
            for i in range(L) :
                wo = record[0]
                w = record[1]
                
                record = [max(wo, w), wo+nums[i]]
        
            return max(record[0], record[1])
        
        
        