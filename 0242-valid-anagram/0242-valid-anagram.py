class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        
        if len(s) != len(t) :
            return False
        
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if x in d1 :
                d1[x] += 1
            else :
                d1[x] = 1
                
            if y in d2 :
                d2[y] += 1
            else :
                d2[y] = 1
        
        if d1 == d2 :
            return True
        else :
            return False