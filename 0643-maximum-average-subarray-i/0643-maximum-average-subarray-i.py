class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        K, N = k, len(nums)
        S = 0
        M = 0

        for k in range(K):
            S += nums[k]
        M = S

        for i in range(N-K):
            S += (nums[K+i] - nums[i])
            M = max(M, S)
        
        return M/K
