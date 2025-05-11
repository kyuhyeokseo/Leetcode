class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        L1, L2 = len(s1), len(s2)
        if L1 > L2:
            return False

        s1 = ''.join(sorted(list(s1)))
        key  = s1
        hint = ''.join(sorted(list(s2[:L1])))
        
        if key == hint:
            return True

        for idx in range(L1, L2):
            IN, OUT = s2[idx], s2[idx-L1]
            hint = self.InNOut(hint, IN, OUT)
            if key == hint:
                return True
        
        return False
        
    def InNOut(self, hint, IN, OUT):
        L = len(hint)

        if IN == OUT:
            return hint

        for i in range(L):
            if hint[i] == OUT:
                hint = hint[:i] + hint[i+1:]
                break
        
        for i in range(L-1):
            if IN <= hint[i]:
                hint = hint[:i] + IN + hint[i:]
                break
        
        if len(hint) < L:
            hint += IN
        return hint