class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0, cnt2 = 0, 0
        i = 0
        
        L = len(nums)
        
        for _ in range(L):
        
            if nums[i] == 0 :
                nums[i], nums[cnt0] = nums[cnt0], nums[i]
                cnt0 += 1
                i += 1
            elif nums[i] == 2 :
                nums[i], nums[L-1-cnt2] = nums[L-1-cnt2], nums[i]
                cnt2 += 1
            else :
                i += 1
        
        #print(nums)
            
            