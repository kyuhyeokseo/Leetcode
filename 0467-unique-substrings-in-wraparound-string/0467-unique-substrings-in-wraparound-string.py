class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        
        rec = {}
        L = len(s)

        prev = ''
        prev_cnt = 0
        ret = 0
        
        for x in range(26):
            rec[chr(ord('a')+x)] = 0

        for idx in range(L):
            if idx == 0 :
                rec[s[idx]] = 1
                prev = s[idx]
                prev_cnt = 1
                ret += prev_cnt
            else :
                if self.prev_base(s[idx]) == s[idx-1]:
                    prev = s[idx]
                    prev_cnt += 1
                    diff = max(0, (prev_cnt - rec[s[idx]]))
                    rec[s[idx]] = max(prev_cnt, rec[s[idx]])
                    ret += diff
                else :
                    prev = s[idx]
                    prev_cnt = 1
                    diff = max(0, (prev_cnt - rec[s[idx]]))
                    rec[s[idx]] = max(prev_cnt, rec[s[idx]])
                    ret += diff
        return ret

    
    def prev_base(self, x):
        if x == 'a':
            return 'z'
        else :
            return chr(ord(x)-1)
    