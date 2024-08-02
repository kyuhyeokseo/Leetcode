class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0 :
            return 0
        
        dp = [999999999999] * (amount+1) 
        dp[0] = 0
            
        for coin in coins :
            for tmp in range(coin, amount + 1) :
                dp[tmp] = min(dp[tmp], dp[tmp-coin] + 1)
        
        if dp[amount] != 999999999999 :
            return dp[amount]
        else :
            return -1

        
        
        
        