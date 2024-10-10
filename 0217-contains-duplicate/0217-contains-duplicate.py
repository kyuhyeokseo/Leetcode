class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        L1 = len(nums)
        L2 = len(list(set(nums)))
        
        #print(L1, L2)
        
        if L1 == L2 :
            return False
        else :
            return True
        
        
        
        
        