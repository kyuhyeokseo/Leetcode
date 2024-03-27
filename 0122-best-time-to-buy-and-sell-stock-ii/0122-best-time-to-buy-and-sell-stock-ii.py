class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        PROFIT = 0
        L = len(prices)
        for i in range(L-1):
            PROFIT += max(0, prices[i+1] - prices[i])
            
        return PROFIT