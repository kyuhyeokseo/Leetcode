class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()

        L = len(nums)
        s = 0
        for i in range(0, L, 2):
            s += nums[i]
        
        return s