class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        ret = ''
        cnt = 0

        s = s.replace('-', '').upper()[::-1]

        for t in s:

            if t != '-':
                if cnt >= k :
                    ret = '-' + ret
                    ret = t + ret
                    cnt = 1
                else :
                    ret = t + ret
                    cnt += 1
        
        return ret
            








