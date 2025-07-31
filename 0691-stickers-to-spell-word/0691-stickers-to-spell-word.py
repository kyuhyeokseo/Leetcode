class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        @lru_cache(None)
        def dfs(target):

            if not target:
                return 0
            
            tCount, ret = Counter(target), inf
            minT = min(tuple(tCount), key = lambda x: tCount[x])

            for sCount in sCounts:
                if sCount[minT] == 0:
                    continue
                
                nxt = dfs(''.join((tCount-sCount).elements()))
                if nxt != -1:
                    ret = min(ret, nxt+1)
            
            return -1 if ret == inf else ret
        
        sCounts = []
        for s in stickers:
            if bool(set(s) & set(target)):
                sCounts.append(Counter(s))

        return dfs(target)

        