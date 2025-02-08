class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        i, j = 0, 0
        cnt = 0

        while i < len(g) and j < len(s):
            target = g[i]
            if target <= s[j] :
                cnt += 1
                i += 1
                j += 1
            else :
                j += 1
        
        return cnt

