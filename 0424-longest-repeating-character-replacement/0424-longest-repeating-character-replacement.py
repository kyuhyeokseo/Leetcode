class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = len(s)
        srt, end = 0, k-1

        # Success : end-srt+1 - MAX <= k

        D = {}
        for i in range(srt, end+1):
            if s[i] in D :
                D[s[i]] += 1
            else :
                D[s[i]] = 1

        if k > 0 :
            MAX = max(D.values())
        else :
            MAX = 0
        
        ret = end -srt +1

        while end < L :

            #print(srt, end, MAX)

            if end -srt +1 -MAX <= k :
                ret = max(ret, end-srt+1)
                if end == L-1 :
                    break

                end += 1
                if s[end] in D :
                    D[s[end]] += 1
                    MAX = max(MAX, D[s[end]])
                else :
                    D[s[end]] = 1
                    MAX = max(MAX, D[s[end]])
            else :
                D[s[srt]] -= 1
                if D[s[srt]] == 0 :
                    del D[s[srt]]
                    srt += 1
                else :
                    if D[s[srt]] + 1 == MAX :
                        MAX = max(MAX, max(D.values()))
                    srt += 1

        return ret
                



