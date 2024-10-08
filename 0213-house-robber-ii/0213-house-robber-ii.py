class Solution:
    def rob(self, nums: List[int]) -> int:
        
        L = len(nums)
        
        if L <= 3 :
            return max(nums)
        
        # Index 0 : 0...0
        # Index 1 : 0...1
        # Index 2 : 1...0
        # Index 3 : 1...1
        
        dp = [[0,0,0,0] for _ in range(L)]
        
        dp[2][0], dp[2][1], dp[2][2], dp[2][3] = nums[1], nums[2], nums[0], nums[0] + nums[2]
        
        for i in range(3, L) :
            n = nums[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + n
            dp[i][2] = max(dp[i-1][2], dp[i-1][3])
            dp[i][3] = dp[i-1][2] + n
            
        return max(dp[-1][:-1])