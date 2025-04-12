class Solution:
    def countArrangement(self, N: int) -> int:
        
        @lru_cache(None)
        def dfs(visited, c):
            if c == 0: return 1

            S = 0
            for n in range(N):
                if not(visited & (1<<n)) and ((n+1) % c == 0 or c % (n+1) == 0):
                    S += dfs(visited ^ (1<<n), c-1)
            return S
        
        return dfs(0, N)
