class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = []
        out = 1
        
        for idx in range(len(nums)) :
            
            dp.append(1)
            
            if idx > 0 :
                N = nums[idx]
                for j in range(0, idx) :
                    if nums[j] < N :
                        dp[idx] = max(dp[idx], dp[j] + 1)
                
                #print(out, dp[idx])
                out = max(out, dp[idx])
                #print(out)
            
        #print(dp)
        return out
        