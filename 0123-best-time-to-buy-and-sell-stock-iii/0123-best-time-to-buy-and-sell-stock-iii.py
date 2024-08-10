class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = len(prices)
        
        if L==1 :
            return 0
        
        dp = [[-99999,-99999,-99999,-99999, -99999] for _ in range(L+1)]
        
        # Nothing
        # With First stock
        # Nothing after Selling First stock
        # With Second stock
        # Nothing after Selling Second stock
        
        dp[0][0] = 0
        
        for i in range(1, L+1):
            dp[i][0] = 0
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i-1])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i-1])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i-1])
            
        out = max(dp[L][0], dp[L][2], dp[L][4])
        return out
        
        
        
        