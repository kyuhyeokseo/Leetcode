class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        out = 0
        X = []
        
        for w in words :
            L = [0] * 26
            S = len(w)
            for u in w :
                if L[ord(u) - ord('a')] == 0 :
                    L[ord(u) - ord('a')] += 1
            
            Y = 0
            for i in range(26):
                Y = (Y<<1) + L[i]    
        
            for x in X :
                y, s = x[0], x[1]
                
                #print(y&Y, s, S, s*S, out)
                if y & Y == 0 :
                    out = max(out, s*S)
        
            X.append([Y, S])
        
        return out
        
        