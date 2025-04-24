class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(groups):
            
            if not groups:
                return 0
            
            (c, l), groups = groups[0], groups[1:]
            ret = l * l + dfs(groups)

            for i, (C, L) in enumerate(groups):
                
                if c == C:
                    ret = max(ret, dfs(groups[:i]) + dfs( ((c, l+L),) + groups[i+1:] ))
            
            return ret

        box_groups = tuple((k, len(list(g))) for k, g in groupby(boxes))
        return dfs(box_groups)