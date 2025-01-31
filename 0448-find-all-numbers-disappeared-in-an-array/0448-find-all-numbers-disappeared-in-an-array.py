class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ret = []
        N = len(nums)
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0 :
                nums[idx] *= -1
        
        for i in range(N):
            if nums[i] > 0 :
                ret.append(i+1)
        
        return ret