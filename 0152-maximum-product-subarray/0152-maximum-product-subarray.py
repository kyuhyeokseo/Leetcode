class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [[-99999, 99999] for _ in range(len(nums)+1)]
        
        dp[0][0] = 1
        dp[0][1] = 1
        
        out = nums[0]
        
        for i in range(1, len(nums)+1) :
            
            num = nums[i-1]
            
            if num > 0 :
                dp[i][0] = max(dp[i][0], num, num * dp[i-1][0])
                dp[i][1] = min(dp[i][1], num * dp[i-1][1])
                out = max(out, dp[i][0])
            
            elif num < 0 :
                dp[i][0] = max(dp[i][0], num, num * dp[i-1][1])
                dp[i][1] = min(dp[i][1], num, num * dp[i-1][0])
                out = max(out, dp[i][0])
            
            else :
                dp[i][0] = dp[i][1] = 0
                out = max(out, dp[i][0])
            
        return out
            
            
        
        
        
        
        