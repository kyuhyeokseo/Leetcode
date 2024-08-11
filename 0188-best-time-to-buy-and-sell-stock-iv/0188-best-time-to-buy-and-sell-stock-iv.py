class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        L = len(prices)
        
        if L==1 :
            return 0
        
        dp = [[-99999 for _ in range(2*k+1)] for _ in range(L+1)]
        
        
        dp[0][0] = 0
        
        for i in range(1, L+1):
            dp[i][0] = 0
            for p in range(1,k+1):
                dp[i][2*p-1] = max(dp[i-1][2*p-1], dp[i-1][2*p-2] - prices[i-1])
                dp[i][2*p] = max(dp[i-1][2*p], dp[i-1][2*p-1] + prices[i-1])
            
            
        out = -1
        for p in range(k+1) :
            out = max(out, dp[L][2*p])
        return out
        
        
        
        
        
        