class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        D = {}
        strs.sort(key = lambda x:-len(x))

        for s in strs:
            if s in D:
                D[s] += 1
            else:
                D[s] = 1
        
        MAX = -1
        for i, s in enumerate(strs):
            if D[s] > 1:
                pass
            else:
                flag = True
                for j in range(i):
                    if self.isin(s, strs[j][:]):
                        flag = False
                        break
                if flag:
                    MAX = max(MAX, len(s))
        
        return MAX

    def isin(self, child, parent):
        C, P = len(child), len(parent)
        c = 0
        for p in range(P):
            if c == C:
                return True
            if parent[p] == child[c]:
                c += 1
        if c == C:
            return True
        else:
            return False
