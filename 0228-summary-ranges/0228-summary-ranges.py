class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        
        cont = 0
        tmp = []
        ans = []
        for i in range(len(nums)) :
            if len(tmp) != 0 :
                if tmp[-1] + 1 != nums[i] :
                    if len(tmp) == 1 :
                        ans.append(str(tmp[-1]))
                    else :
                        ans.append(str(tmp[0])+'->'+str(tmp[-1]))
                    tmp = []
            
            tmp.append(nums[i])
            
        
        if len(tmp) != 0 :
                if tmp[-1] + 1 != nums[i] :
                    if len(tmp) == 1 :
                        ans.append(str(tmp[-1]))
                    else :
                        ans.append(str(tmp[0])+'->'+str(tmp[-1]))
        
        return ans
        
        
        
        
        
        
        