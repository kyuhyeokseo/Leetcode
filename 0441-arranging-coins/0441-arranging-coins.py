class Solution:
    def arrangeCoins(self, n: int) -> int:
        ret = ((8*n+1) ** 0.5 - 1) / 2
        return int(ret) 