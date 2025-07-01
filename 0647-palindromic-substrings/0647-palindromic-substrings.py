class Solution:
    def countSubstrings(self, s: str) -> int:
        
        cnt = 0
        L = len(s)

        for center in range(L):
            l = min(center, L-center-1)
            for i in range(l, -1, -1):
                if s[center-i:center+i+1] == s[center-i:center+i+1][::-1]:
                    #print(s[center-i:center+i+1], center, i)
                    cnt += (i+1)
                    break
        
        if L > 1:
            for center in range(L-1):
                l = min(center, L-2-center)
                for i in range(l, -1, -1):
                    if s[center-i:center+i+2] == s[center-i:center+i+2][::-1]:
                        #print(s[center-i:center+i+1], center, i)
                        cnt += (i+1)
                        break
        
        return cnt