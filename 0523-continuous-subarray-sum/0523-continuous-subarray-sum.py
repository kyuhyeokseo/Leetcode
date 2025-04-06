class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 1:
            return False

        D = {}
        D[0] = 0

        S = 0
        for i in range(len(nums)):
            idx = i+1
            S += nums[i]
            key = S % k
            if key in D:
                if (idx - D[key]) > 1:
                    return True
            else:
                D[key] = idx
        return False

        