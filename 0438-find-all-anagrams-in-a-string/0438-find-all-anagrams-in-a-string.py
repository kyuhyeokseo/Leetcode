class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ret = []

        pD, sD = {}, {}
        for pp in p :
            if pp in pD :
                pD[pp] += 1
            else :
                pD[pp] = 1
        
        keys = list(pD.keys())

        for ss in s[:len(p)] :
            if ss in sD :
                sD[ss] += 1
            else :
                sD[ss] = 1

        for i in range(len(s)-len(p)+1):
            srt, end = i, i+len(p)-1

            if srt > 0 :
                sD[s[srt-1]] -= 1
                if sD[s[srt-1]] == 0 :
                    del sD[s[srt-1]]
                
                if s[end] in sD :
                    sD[s[end]] += 1
                else :
                    sD[s[end]] = 1

            flag = True
            for k in keys :
                if not(k in sD and sD[k] == pD[k]):
                    flag = False
                    break
            if flag :
                ret.append(srt)
            
        return ret


