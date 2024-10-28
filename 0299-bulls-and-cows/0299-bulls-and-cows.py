class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        L = len(secret)
        
        dicBs, dicBg, cntA = {}, {}, 0
        
        for i in range(L):
            s = secret[i]
            g = guess[i]
            
            if s in dicBs :
                dicBs[s] += 1
            else :
                dicBs[s] = 1
                
            if g in dicBg :
                dicBg[g] += 1
            else :
                dicBg[g] = 1
                
            if s == g :
                cntA += 1
        
        cntAB = 0
        for k in dicBs.keys():
            if k in dicBg :
                cntAB += min(dicBs[k], dicBg[k])
        
        cntB = cntAB - cntA
        
        return (str(cntA) + 'A' + str(cntB) + 'B')
        
        
        
        