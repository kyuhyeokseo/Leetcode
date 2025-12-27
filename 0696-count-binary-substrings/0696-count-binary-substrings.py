class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        cum = 1
        now = s[0]
        rec = []

        for i in range(1, len(s)):
            if s[i] == now:
                cum += 1
            else:
                rec.append(cum)
                cum = 1
                now = s[i]
        rec.append(cum)

        ret = 0
        for i in range(len(rec)-1):
            ret += min(rec[i], rec[i+1])
        
        return ret