class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        ret = 1
        cnt = 1
        last = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
                last = nums[i]
            else:
                cnt = 1
                last = nums[i]
            
            ret = max(ret, cnt)

        return ret
