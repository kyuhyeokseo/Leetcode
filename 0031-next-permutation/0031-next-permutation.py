class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        L = len(nums)
        
        flag = False
        sep = 0
        
        if L >= 2 :
            
            for i in range(L-1, 0, -1) :
                if nums[i-1] < nums[i] :
                    flag = True
                    sep = i
                    break
            
            if flag == False :
                nums.sort()
            
            else :

                M = nums[sep-1]
                nums[sep-1], nums[sep] = nums[sep], nums[sep-1]
                
                LL = len(nums[sep:])
                
                for j in range(LL) :
                    if nums[sep+j] > M :
                        if nums[sep-1] > nums[sep+j] :
                            nums[sep-1], nums[sep+j] = nums[sep+j], nums[sep-1]
                 
                #print(nums, LL)
                
                if LL == 1 :
                    pass
                else :
                    for x in range(LL-1, 0, -1) :
                        for k in range(x) :
                            if nums[sep+k] > nums[sep+k+1] :
                                nums[sep+k], nums[sep+k+1] = nums[sep+k+1], nums[sep+k]
                        

                
                