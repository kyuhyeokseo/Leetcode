class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        L = len(coins)
        coins = sorted(coins, reverse = True)

        dp = [[0 for _ in range(amount + 1)] for _ in range(L)]

        cums = [0]

        for i in range(L):

            c = coins[i]
            new_cums = set()

            if i == 0:
                for cum in cums:
                    j = 0
                    while cum + j*c <= amount:
                        dp[i][cum+j*c] += 1
                        new_cums.add(cum + j*c)
                        j += 1
            
            else:
                for cum in cums:
                    j = 0
                    while cum + j*c <= amount:
                        dp[i][cum+j*c] += dp[i-1][cum]
                        new_cums.add(cum + j*c)
                        j += 1
                    
            cums = list(new_cums)[:]
        
        return dp[-1][-1]

        