class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            return 0

        L = len(nums)

        prefix = [1]
        for l in range(L):
            prefix.append(prefix[-1] * nums[l])

        ret = 0
        i = 0
        
        for j in range(1, L+1):
            while i < j and (prefix[j] // prefix[i] >= k):
                i += 1
            ret += j-i
        
        return ret






