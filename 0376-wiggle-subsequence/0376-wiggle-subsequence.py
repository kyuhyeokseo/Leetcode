class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        if N == 1 :
            return 1
        
        out = 1
        target = nums[0]
        
        flow = ''
        for i in range(1, N):
            if target == nums[i]:
                continue
            elif target > nums[i] :
                if flow != '-' :
                    out += 1
                flow = '-'
                target = nums[i]
            else :
                if flow != '+' :
                    out += 1
                flow = '+'
                target = nums[i]
                
            #print(out, nums[i])     
                
        return out