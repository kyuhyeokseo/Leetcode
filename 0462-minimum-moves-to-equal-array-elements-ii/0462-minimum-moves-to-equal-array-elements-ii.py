class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        N = len(nums)
        nums.sort()

        ret = 0
        for i in range((N+1)//2):
            ret += (nums[N-1-i] - nums[i])

        return ret
