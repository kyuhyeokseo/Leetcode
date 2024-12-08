class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        self.dp = [-1 for _ in range(target+1)]
        self.nums = nums[:]
        
        return self.combS(target)
    
    def combS(self, N):
        if self.dp[N] >= 0 :
            return self.dp[N]
        
        cnt = 0
        for n in self.nums :
            if N-n > 0 :
                cnt += (self.combS(N-n))
            elif N-n == 0 :
                cnt += 1
        self.dp[N] = cnt
                
        return cnt
        
        
        
        
        
        