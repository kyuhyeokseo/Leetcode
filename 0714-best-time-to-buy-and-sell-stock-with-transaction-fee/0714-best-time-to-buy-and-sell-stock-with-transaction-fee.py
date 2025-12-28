class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        INF = 10 ** 6
        rec = [-(prices[0]+fee), 0]

        if len(prices) == 1:
            return 0

        for p in prices[1:]:
            rec[0], rec[1] = max(rec[1] - (p+fee) , rec[0]), max(rec[1], rec[0]+p)

        return rec[1]