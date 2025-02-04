class Solution:
    def minMoves(self, nums: List[int]) -> int:
        N = len(nums)
        MIN = nums[0]
        SUM = 0
        for n in nums :
            MIN = min(MIN, n)
            SUM += n
        
        return SUM - MIN * N