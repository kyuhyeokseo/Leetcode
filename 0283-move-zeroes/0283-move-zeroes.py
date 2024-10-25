class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        L = len(nums)
        
        for i in range(L):
            
            if nums[i] == 0 :
                
                findNonZero = False
                for j in range(i+1, L):
                    if nums[j] != 0 :
                        nums[i], nums[j] = nums[j], nums[i]
                        findNonZero = True
                        break

                if findNonZero == False :
                    break
                    
                    
            #print(nums)
    