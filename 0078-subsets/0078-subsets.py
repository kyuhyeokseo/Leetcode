class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = [[]]
        L = len(nums)
        
        for i in range(L) :
            
            n = nums[i]
            out2 = out[:]
            
            #print(out)
            for item in out:
                #print(item)
                item_tmp = item[:]
                item_tmp.append(n)
                out2.append(item_tmp)
            
            out = out2[:]
        
        return out
        
        
        
        
        
        