class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
    
        return_value = []
        out = [0 for _ in range((1<<20))]
        L = len(s)
        
        D = {}
        D['A'], D['C'], D['G'], D['T'] = 0, 1, 2, 3
        
        if L < 10 :
            return []
        
        tmp = 0
        for i in range(L):
            tmp *= 4
            tmp += D[s[i]]
            tmp %= (1<<20)
            #print(i, tmp, out[i])
            
            if i >= 9 :
                if out[tmp] == 0 :
                    out[tmp] += 1
                elif out[tmp] == 1 :
                    out[tmp] += 1
                    return_value.append(s[i-9:i+1])
                else :
                    out[tmp] += 1
        
        return return_value