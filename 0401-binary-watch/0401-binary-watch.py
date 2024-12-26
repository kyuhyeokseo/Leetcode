from collections import defaultdict

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        ret = []
        
        D = defaultdict(list)
        
        D[0] = [0]
        for x in range(1, 60):
            n = x
            cnt1 = 0
            while n :
                n = n & (n-1)
                cnt1 += 1
            D[cnt1].append(x)
        
        
        for H in range(0, turnedOn+1):
            
            M = turnedOn - H
            
            if H > 3 or M > 5 :
                continue
            
            else :
                Hs, Ms = D[H], D[M]
                for h in Hs :
                    if h < 0 or h > 11 :
                        continue
                    for m in Ms :
                        if m < 0 or m > 59 :
                            continue
                        
                        tmp = f'{h}:{m:02d}'
                        ret.append(tmp)
            
        return ret
            
        
        
        
        
        
        