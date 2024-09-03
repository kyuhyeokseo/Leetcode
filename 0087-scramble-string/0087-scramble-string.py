class Solution:
    
    D = {}
    
    def isScramble(self, s1: str, s2: str) -> bool:
        
        L1 = len(s1)
        L2 = len(s2)
        
        if s1 == s2 :
            return True
        
        X = [0] * 26
        Y = [0] * 26
        Z = [0] * 26
        
        if s1 + s2 in self.D:
            return self.D[s1+s2]
        
        for i in range(1,L1):
            j = L1-i
            
            X[ord(s1[i-1]) - ord('a')] += 1
            Y[ord(s2[i-1]) - ord('a')] += 1
            Z[ord(s2[j]) - ord('a')] += 1
            
            if X == Y and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.D[s1 + s2] = True
                return True
            
            if X == Z and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                self.D[s1 + s2] = True
                return True
            
        self.D[s1 + s2] = False
        return False