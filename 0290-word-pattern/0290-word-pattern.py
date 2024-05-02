class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split(' ')
        
        if len(t) != len(pattern):
            return False
        
        d1, d2 = {}, {}
        
        for i in range(len(t)):
            tmp1 = pattern[i]
            tmp2 = t[i]
            
            if tmp1 not in d1 :
                d1[tmp1] = tmp2
            
            elif tmp1 in d1 :
                if d1[tmp1] != tmp2 :
                    return False
            
            if tmp2 not in d2 :
                d2[tmp2] = tmp1
            
            elif tmp2 in d2 :
                if d2[tmp2] != tmp1 :
                    return False
        
        return True