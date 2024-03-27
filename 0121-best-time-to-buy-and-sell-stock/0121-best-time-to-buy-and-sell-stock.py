class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 10 ** 6
        sell = -1
        L = len(prices)
        MAX = -99
        
        for i in range(L):
            if i == 0 :
                buy = prices[i]
            else :
                MAX = max(MAX, prices[i]- buy)
                buy = min(buy, prices[i])
                
                
        MAX = max(0, MAX)
        return MAX
        
        
        
        
        