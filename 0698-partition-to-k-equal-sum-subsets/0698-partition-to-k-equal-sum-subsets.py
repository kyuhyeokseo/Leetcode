class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if len(nums) < k or sum(nums) % k:
            return False
        
        N = len(nums)

        @cache
        def dp(mask, curr):
            if mask == 0:
                return curr == 0
            elif curr == 0:
                return dp(mask, sum(nums)//k)
            else:
                for bit in range(len(nums)):
                    if mask & (1<<bit):
                        if nums[bit] <= curr and dp(mask ^ (1<<bit), curr-nums[bit]):
                            return True
                return False
        
        return dp((1<<N)-1, sum(nums)//k)






