import heapq

class Solution:
    def shoppingOffers(self, price: List[int], specials: List[List[int]], needs: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(needs):

            cost = sum(map(mul, needs, price))

            for special in specials:
                specialPrice = special[-1]
                tmp = tuple(map(sub, needs, special[:-1]))

                if min(tmp) < 0:
                    continue
                else:
                    cost = min(cost, dfs(tmp) + specialPrice)
            
            return cost
        
        return dfs(tuple(needs))


        