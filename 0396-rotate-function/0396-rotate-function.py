class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        if N == 1 :
            return 0
        
        S = 0
        tmp = 0
        for i in range(N):
            tmp += i * nums[i]
            S += nums[i]
            
        ret = tmp
        
        for i in range(N-1, -1, -1):
            tmp += (S - N * nums[i])
        
            ret = max(ret, tmp)
        
        return ret
        
        
        
        
        
        
        
        
        
        