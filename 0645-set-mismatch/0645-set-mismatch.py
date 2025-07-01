class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        together, dup = 0, None

        for i in range(len(nums)):

            together ^= (i+1)
            if nums[i]>0:
                together ^= nums[i]
                if nums[nums[i]-1] < 0:
                    dup = nums[i]
                nums[nums[i]-1] *= -1
            else:
                together ^= (-nums[i])
                if nums[(-nums[i])-1] < 0:
                    dup = -nums[i]
                nums[(-nums[i])-1] *= -1
            
            #print(nums, together, dup)
        
        return [dup, dup^together]
        
        